import logging

LOG_FILE = "redshadow.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_warning(message):
    logging.warning(message)
    print(f"[WARNING] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")