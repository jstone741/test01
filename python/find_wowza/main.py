import requests

def get_server_header(ip):
    url = f"http://{ip}:1935/crossdomain.xml"
    try:
        response = requests.get(url, timeout=5)
        server_header = response.headers.get('Server', 'No Server Header')
        return server_header
    except requests.RequestException as e:
        return f"Request failed: {e}"

def main():
    with open('iplist.txt', 'r') as ip_file, open('result.txt', 'w') as result_file:
        for line in ip_file:
            ip = line.strip()
            if ip:
                server_header = get_server_header(ip)
                result_file.write(f"{ip}: {server_header}\n")

if __name__ == "__main__":
    main()