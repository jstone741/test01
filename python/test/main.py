import tkinter as tk
import subprocess
import pyautogui
import time

# Putty 및 plink 실행 경로 설정
putty_path = r'C:\Program Files (x86)\PuTTY\putty.exe'

# 숫자를 Shift된 특수문자로 변환하는 함수 (예: 1 -> !, 8 -> *, 3 -> #)
def shift_ip_part(ip_first_part):
    shift_map = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
    return ''.join(shift_map.get(char, char) for char in ip_first_part)

# 사용자와 root 비밀번호 생성 함수
def generate_passwords(user_password, root_password, ip):
    ip_parts = ip.split('.')
    ip_first_part = ip_parts[0]  # IP 앞자리 (예: 183)
    ip_last_part = ip_parts[-1]  # IP 뒷자리 (예: 207)

    # Shift된 IP의 앞자리를 변환
    shifted_ip = shift_ip_part(ip_first_part)

    # 비밀번호 조건 적용
    user_password_modified = f"{user_password}{shifted_ip}{ip_last_part}"
    root_password_modified = f"{root_password}{shifted_ip}{ip_last_part}"

    return user_password_modified, root_password_modified

# Putty 실행 함수
def run_putty(ip, user, password, root_password):
    # 비밀번호 생성
    user_password_modified, root_password_modified = generate_passwords(password, root_password, ip)

    # PuTTY 실행 명령어 구성
    putty_command = f'"{putty_path}" -ssh {user}@{ip} -pw {user_password_modified}'

    # PuTTY 창을 실행
    subprocess.Popen(putty_command, shell=True)

    # PuTTY 창이 열릴 때까지 잠시 대기
    time.sleep(0.8)  # 필요에 따라 시간을 조정하세요

    # su - 명령어 입력
    pyautogui.typewrite('su -', interval=0.1)  # 타이핑 속도 조정
    pyautogui.press('enter')

    # su - 이후 잠시 대기
    time.sleep(0.2)  # 필요에 따라 시간을 조정하세요

    # root_password_modified 값을 입력
    pyautogui.typewrite(root_password_modified, interval=0.1)  # 타이핑 속도 조정
    pyautogui.press('enter')

# 여러 서버에 접속하는 함수
def connect_servers(event=None):  # event 매개변수는 엔터 키 이벤트에서 사용됨
    # 입력된 IP 목록을 엔터로 구분하여 분리
    ip_list = ip_entry.get("1.0", tk.END).strip().split('\n')
    user = id_entry.get()
    user_password = passwd_entry.get()
    root_password = root_passwd_entry.get()

    for ip in ip_list:
        ip = ip.strip()  # 각 IP 주소의 앞뒤 공백 제거
        # Putty 창을 띄움
        run_putty(ip, user, user_password, root_password)

# Tkinter GUI 생성
root = tk.Tk()
root.title("Multi Putty Launcher with Root Access")
root.geometry("600x500")  # 창 크기를 조정

# IP 입력 (여러 줄 입력 가능하도록 Text 위젯 사용)
tk.Label(root, text="IP Addresses (enter-separated):").pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=5)

ip_entry = tk.Text(frame, height=10, width=50)  # 여러 줄로 입력할 수 있도록 설정
ip_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 스크롤바 추가
scrollbar = tk.Scrollbar(frame, command=ip_entry.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
ip_entry.config(yscrollcommand=scrollbar.set)

# ID 입력
tk.Label(root, text="User ID:").pack(pady=5)

# 기본값 설정 (blacktiger)
id_default = tk.StringVar(value="blacktiger")
id_entry = tk.Entry(root, width=50, textvariable=id_default)
id_entry.pack(pady=5)

# 비밀번호 입력
tk.Label(root, text="User Password:").pack(pady=5)
passwd_entry = tk.Entry(root, show="*", width=50)
passwd_entry.pack(pady=5)

# root 비밀번호 입력
tk.Label(root, text="Root Password:").pack(pady=5)
root_passwd_entry = tk.Entry(root, show="*", width=50)
root_passwd_entry.pack(pady=5)

# root 비밀번호 입력 필드에서 엔터 키가 눌리면 connect_servers 함수 호출
root_passwd_entry.bind('<Return>', connect_servers)

# 서버 접속 버튼 (크기 조정)
connect_button = tk.Button(root, text="Connect", command=connect_servers, height=2, width=20)  # 버튼 크기를 키움
connect_button.pack(pady=20)

root.mainloop()
