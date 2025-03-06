import requests
import socket

def run():
    target = input("Enter target domain/IP: ").strip()

    if not target:
        print("Invalid target input.")
        return

    print(f"Running reconnaissance on {target}...")

    try:
        ip = socket.gethostbyname(target)
        print(f"IP Address: {ip}")

        response = requests.get(f"https://api.hackertarget.com/whois/?q={target}")
        
        if response.status_code == 200:
            print("WHOIS Data:\n", response.text)
        else:
            print(f"WHOIS lookup failed with status code {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
