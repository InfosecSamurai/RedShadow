import requests
import socket
import logging
import re

def validate_target(target):
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    domain_pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(ip_pattern, target) or re.match(domain_pattern, target)

def get_whois_data(target):
    try:
        response = requests.get(f"https://api.hackertarget.com/whois/?q={target}", timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"WHOIS lookup failed with status code {response.status_code}"
    except requests.RequestException as e:
        return f"Error fetching WHOIS data: {e}"

def get_dns_records(target):
    try:
        response = requests.get(f"https://api.hackertarget.com/dnslookup/?q={target}", timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"DNS lookup failed with status code {response.status_code}"
    except requests.RequestException as e:
        return f"Error fetching DNS records: {e}"

def run():
    logging.basicConfig(filename="reconnaissance.log", level=logging.INFO)
    logging.info("Starting reconnaissance module...")

    target = input("Enter target domain/IP: ").strip()

    if not validate_target(target):
        print("Invalid target input. Please enter a valid domain or IP address.")
        logging.error("Invalid target input provided.")
        return

    print(f"Running reconnaissance on {target}...")
    logging.info(f"Target: {target}")

    try:
        ip = socket.gethostbyname(target)
        print(f"IP Address: {ip}")
        logging.info(f"Resolved IP Address: {ip}")

        whois_data = get_whois_data(target)
        print("WHOIS Data:\n", whois_data)
        logging.info("WHOIS Data retrieved.")

        dns_records = get_dns_records(target)
        print("DNS Records:\n", dns_records)
        logging.info("DNS Records retrieved.")

    except socket.gaierror as e:
        print(f"Error resolving target: {e}")
        logging.error(f"Error resolving target: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error: {e}")

    print("Reconnaissance complete.")
    logging.info("Reconnaissance module completed.")