import tkinter as tk
import hmac
import hashlib
import base64
import urllib.parse


def generate_signed_url():
    key = key_entry.get()
    base_url = base_url_entry.get()
    policy_expire = policy_expire_entry.get()

    # 기본 Policy 값 설정
    policy = f'{{"url_expire":{policy_expire}}}'

    # base64url encoding (RFC 4648)
    policy_base64 = base64.urlsafe_b64encode(policy.encode()).decode().rstrip('=')
    policy_url = f"{base_url}?policy={policy_base64}"

    # HMAC-SHA1 서명 생성
    signature = hmac.new(key.encode(), policy_url.encode(), hashlib.sha1).digest()
    signature_base64 = base64.urlsafe_b64encode(signature).decode().rstrip('=')

    # 최종 URL 생성
    signed_url = f"{policy_url}&signature={signature_base64}"

    # 결과 출력
    result_text.delete(1.0, tk.END)  # 기존 내용 삭제
    result_text.insert(tk.END, signed_url)  # 새로운 결과 삽입


# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Signed URL Generator")

# 창 크기 조정
root.geometry("600x400")

# 입력 필드 및 라벨
tk.Label(root, text="HMAC Key:", anchor='w').pack(fill='x')
key_entry = tk.Entry(root, width=80)
key_entry.pack(fill='x', padx=10, pady=5)

tk.Label(root, text="Base URL:", anchor='w').pack(fill='x')
base_url_entry = tk.Entry(root, width=80)
base_url_entry.pack(fill='x', padx=10, pady=5)

tk.Label(root, text="Policy Expire:", anchor='w').pack(fill='x')
policy_expire_entry = tk.Entry(root, width=80)
policy_expire_entry.pack(fill='x', padx=10, pady=5)

# 생성 버튼
generate_button = tk.Button(root, text="Generate", command=generate_signed_url)
generate_button.pack(pady=10)

# 결과 텍스트 창
result_text = tk.Text(root, height=5, width=80)
result_text.pack(fill='both', padx=10, pady=10, expand=True)

# Tkinter 윈도우 실행
root.mainloop()
