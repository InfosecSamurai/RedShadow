import requests
import socket

def run():
    target = input("Enter target domain/IP: ")
    print(f"Running reconnaissance on {target}...")

    try:
        ip = socket.gethostbyname(target)
        print(f"IP Address: {ip}")
        response = requests.get(f"https://api.hackertarget.com/whois/?q={target}")
        print("WHOIS Data:\n", response.text)
    except Exception as e:
        print(f"Error: {e}")