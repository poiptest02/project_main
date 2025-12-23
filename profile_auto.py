import subprocess
import sys
import re
import time
import json
from ppadb.client import Client as AdbClient

adb_conf = dict(host="127.0.0.1", port=5037)
adb = AdbClient(**adb_conf)
devices = adb.devices()

device = devices[0]

json_path = r"C:\project_main\profile.json"

with open(json_path, "r", encoding = "utf-8") as json_file:
    json_data = json.load(json_file)

for i in range(100):
    device.shell(f"input tap {json_data[0]["profile_X"]} {json_data[0]["profile_Y"]}")
    time.sleep(2)
    device.shell(f"input tap {json_data[1]["profile1_X"]} {json_data[1]["profile1_Y"]}")
    time.sleep(30)
    device.shell(f"input tap {json_data[0]["profile_X"]} {json_data[0]["profile_Y"]}")
    time.sleep(2)
    device.shell(f"input tap {json_data[2]["profile2_X"]} {json_data[2]["profile2_Y"]}")
    