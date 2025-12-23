import subprocess
import sys
import re
import time
import json
from ppadb.client import Client as AdbClient
import os
import shutil

# 기본 ppadb 설정
adb_conf = dict(host="127.0.0.1", port=5037)
adb = AdbClient(**adb_conf)
devices = adb.devices()

# device 객체 생성
device = devices[0]

# 결과 이미지 저장 경로
save_pa = input("저장 경로 삽입")
save_path = f"{save_pa}result.png"

# 기존 결과 이미지 파일 삭제
if os.path.exists(save_pa):
    shutil.rmtree(save_pa)

os.makedirs(save_pa)

# time stamp 객체 생성
timestamp = time.strftime("%Y%m%d_%H%M%S")

''' 위에 부분까지는 공통 요소'''

# json 파일 경로
json_path = input("json 파일 경로 삽입")

''' 위에 부분까지는 json 파일 경로'''

with open(json_path, "r", encoding = "utf-8") as json_file:
    json_data = json.load(json_file)

for i in range(1):

    for idx, point in enumerate(json_data):

        x = point["x"]
        y = point["y"]

        command = f"input tap {x} {y}"
        device.shell(command)


        '''바이너리 저장 코드(앞에 디스플레이 ID 를 )'''
        # 1. 스크린샷 바이너리 원본 가져오기
        raw_data = device.screencap()
        
        # 2. PNG 시그니처 위치 찾기 (\x89PNG)
        png_header = b'\x89PNG' # byte 객체로 변환
        start_index = raw_data.find(png_header) 
        
        if start_index != -1:
            # 시그니처 시작점부터 끝까지만 슬라이싱 (Warning 제거)
            clean_data = raw_data[start_index:]
            
            # 3. 깨끗한 데이터만 저장
            file_full_path = f"{save_pa}\\result_{idx}_{timestamp}.png" # 확장자 png 권장
            with open(file_full_path, "wb") as file:
                file.write(clean_data)
            print(f"!!!저장 완료: {file_full_path}")
        else:
            print("!!! PNG 헤더를 찾을 수 없습니다. 데이터가 완전히 잘못되었습니다.")

        

''' 자동화 코드 '''

