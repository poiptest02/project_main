import subprocess
import sys
import re

# 경로???
INPUT_DEVICE_PATH = "/dev/input/event0"
# -------------------
command_touch_on = ['adb', 'shell', 'settings', 'put', 'system', 'show_touches', '1']
command_touch_off = ['adb', 'shell', 'settings', 'put', 'system', 'show_touches', '0']

command_GIO_On= ['adb', 'shell', 'settings', 'put', 'system', 'pointer_location', '1']
command_GIO_Off = ['adb', 'shell', 'settings', 'put', 'system', 'pointer_location', '0']
# -------------------------------------------------------
subprocess.run(command_touch_on)
subprocess.run(command_GIO_On)
# subprocess.run(command_touch_off)
# subprocess.run(command_GIO_Off)

# -------------------------------------------------------
print("-------------좌표 기록 시작---------------")



subprocess.Popen('adb shell getevent -lt /dev/input/event0 | findstr "ABS_MT_POSITION_"', shell=True, text=True)




# ㅅㅄㅄㅄㅄㅄㅄㅅ



# 시발 윈도우에서는 adb 명령어에 홑따옴표 안먹힌다는걸 3일만에 알다니 개 병신같네



# 1. 터치할 좌표를 확인했다고 가정 (예: X=500, Y=800)
# tap_x = 1354
# tap_y = 430

# 2. ppadb device 객체를 사용하여 실행
# device.shell("input tap [X좌표] [Y좌표]")
# device.shell(f"input tap {tap_x} {tap_y}")
# print(f"좌표 ({tap_x}, {tap_y})에 탭 명령 전송 완료.")
