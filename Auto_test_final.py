import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
import json
import os
import shutil
from ppadb.client import Client as AdbClient

class AdbMacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADB 자동화 툴 v1.0")
        self.root.geometry("500x400")

        # --- UI 구성 ---
        # 1. 저장 경로 선택
        tk.Label(root, text="저장 경로:").pack(pady=5)
        self.save_path_entry = tk.Entry(root, width=50)
        self.save_path_entry.pack(padx=10)
        tk.Button(root, text="폴더 선택", command=self.select_folder).pack(pady=2)

        # 2. JSON 파일 선택
        tk.Label(root, text="JSON 파일:").pack(pady=5)
        self.json_path_entry = tk.Entry(root, width=50)
        self.json_path_entry.pack(padx=10)
        tk.Button(root, text="파일 선택", command=self.select_file).pack(pady=2)

        # 3. 실행 버튼 및 로그 창
        self.start_btn = tk.Button(root, text="매크로 시작", bg="green", fg="white", 
                                   command=self.start_macro_thread, height=2, width=20)
        self.start_btn.pack(pady=20)

        self.log_text = tk.Text(root, height=10, width=60)
        self.log_text.pack(padx=10, pady=10)

    def log(self, message):
        """로그 창에 메시지 출력"""
        self.log_text.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log_text.see(tk.END)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, folder)

    def select_file(self):
        file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file:
            self.json_path_entry.delete(0, tk.END)
            self.json_path_entry.insert(0, file)

    def start_macro_thread(self):
        """UI가 멈추지 않도록 별도 쓰레드에서 실행"""
        t = threading.Thread(target=self.run_macro)
        t.daemon = True
        t.start()

    def run_macro(self):
        save_pa = self.save_path_entry.get()
        json_path = self.json_path_entry.get()

        if not save_pa or not json_path:
            messagebox.showwarning("경고", "모든 경로를 입력해주세요!")
            return

        try:
            self.log("ADB 연결 시도 중...")
            adb = AdbClient(host="127.0.0.1", port=5037)
            devices = adb.devices()
            if not devices:
                self.log("❌ 연결된 디바이스가 없습니다!")
                return
            device = devices[0]

            # 기존 폴더 삭제 및 생성
            if os.path.exists(save_pa):
                shutil.rmtree(save_pa)
            os.makedirs(save_pa)

            with open(json_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)

            timestamp = time.strftime("%Y%m%d_%H%M%S")
            
            for idx, point in enumerate(json_data):
                x, y = point["x"], point["y"]
                device.shell(f"input tap {x} {y}")
                self.log(f"탭 실행: {x}, {y}")

                # 스크린샷 로직
                raw_data = device.screencap()
                png_header = b'\x89PNG'
                start_index = raw_data.find(png_header)

                if start_index != -1:
                    clean_data = raw_data[start_index:]
                    file_name = os.path.join(save_pa, f"result_{idx}_{timestamp}.png")
                    with open(file_name, "wb") as f:
                        f.write(clean_data)
                    self.log(f"📸 저장 완료: {file_name}")
                
                time.sleep(0.5)

            self.log("✅ 모든 작업이 완료되었습니다!")
            messagebox.showinfo("완료", "매크로가 끝났습니다.")

        except Exception as e:
            self.log(f"❌ 오류 발생: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdbMacroApp(root)
    root.mainloop()