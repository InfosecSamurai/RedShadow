import os
import logging

logging.basicConfig(filename="config.log", level=logging.INFO)
logging.info("Loading configuration...")

LOG_PATH = "logs/"
REPORT_PATH = "reports/"

try:
    os.makedirs(LOG_PATH, exist_ok=True)
    os.makedirs(REPORT_PATH, exist_ok=True)
    logging.info(f"Directories created: {LOG_PATH}, {REPORT_PATH}")
except OSError as e:
    logging.error(f"Error creating directories: {e}")
    raise

API_KEYS = {
    "shodan": os.getenv("SHODAN_API_KEY", ""),
    "virustotal": os.getenv("VT_API_KEY", "")
}

if not API_KEYS["shodan"]:
    logging.warning("Shodan API key not found. Some features may be limited.")
if not API_KEYS["virustotal"]:
    logging.warning("VirusTotal API key not found. Some features may be limited.")

logging.info("Configuration loaded successfully.")