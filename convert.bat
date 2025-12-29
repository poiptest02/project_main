@echo off
echo [ 터치 좌표 실시간 10진수 변환 ]
echo 기기 연결을 확인하고 터치해 주세요...
echo ------------------------------------------

:: 파워쉘을 이용해 실시간 스트리밍 처리를 합니다.
powershell -Command "adb shell getevent -lt /dev/input/event0 | ForEach-Object { if ($_ -match 'ABS_MT_POSITION_(X|Y)\s+([0-9a-f]+)') { $type = $matches[1]; $hex = $matches[2]; $dec = [Convert]::ToInt32($hex, 16); Write-Host \"[$type] $dec (0x$hex)\" } }"

pause