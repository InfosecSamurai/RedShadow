import logging
import sys

LOG_FILE = "redshadow.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logging.getLogger().addHandler(console_handler)

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_warning(message):
    logging.warning(message)
    print(f"[WARNING] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def log_debug(message):
    logging.debug(message)
    print(f"[DEBUG] {message}")

def log_critical(message):
    logging.critical(message)
    print(f"[CRITICAL] {message}")

def log_exception(message):
    logging.exception(message)
    print(f"[EXCEPTION] {message}")

if __name__ == "__main__":
    log_info("This is an info message.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")
    log_debug("This is a debug message.")
    log_critical("This is a critical message.")
    try:
        1 / 0
    except Exception as e:
        log_exception("An exception occurred.")