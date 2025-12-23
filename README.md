ctypes.windll.shell32.ShellExecuteW(
    None,           # ① hwnd
    "runas",        # ② lpOperation
    cmdStart,       # ③ lpFile
    None,           # ④ lpParameters
    None,           # ⑤ lpDirectory
    1               # ⑥ nShowCmd
)
① hwnd (Window Handle)
설명: 어떤 창을 부모로 삼아서 UAC 창을 띄울지 지정

None 이면 부모 창 없이 새로 팝업

초보는 그냥 None 쓰면 됨

② lpOperation (작업 유형)
설명: 파일을 어떻게 열지 지정

"open" → 일반 열기

"runas" → 관리자 권한으로 실행 (UAC)

"edit" → 편집용으로 열기 등

관리자 권한이 필요하면 무조건 "runas" 사용

③ lpFile (실행 파일/문서 경로)
설명: 실제로 열거나 실행할 파일 경로

예:

r"C:\Windows\System32\cmd.exe" → CMD 실행

r"C:\Users\Me\Desktop\test.txt" → 메모장 등 기본 앱으로 열림

반드시 전체 경로 권장

④ lpParameters (실행 인자)
설명: 프로그램 실행 시 전달할 옵션/파일 이름

예: cmd.exe /k dir → CMD 열 때 바로 dir 실행

필요 없으면 None

⑤ lpDirectory (작업 디렉토리)
설명: 프로그램이 실행될 기본 경로

예: 어떤 파일을 열 때 기본 폴더 위치 지정

필요 없으면 None → 기본값 사용

⑥ nShowCmd (창 표시 방식)
설명: 프로그램 창을 어떻게 표시할지 결정

일반적인 값:

1 → SW_SHOWNORMAL (기본 창 크기)

0 → SW_HIDE (숨김)

3 → SW_MAXIMIZE (최대화)

2 → SW_MINIMIZE (최소화)

초보는 그냥 1 쓰면 됨