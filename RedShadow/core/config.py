import os

LOG_PATH = "logs/"
REPORT_PATH = "reports/"
API_KEYS = {
    "shodan": os.getenv("SHODAN_API_KEY", ""),
    "virustotal": os.getenv("VT_API_KEY", "")
}