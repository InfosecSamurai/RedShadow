import json
import datetime

def run():
    report = {
        "date": str(datetime.datetime.now()),
        "findings": ["SQL Injection on target.com", "Open SSH Port 22"]
    }
    with open("reports/report.json", "w") as file:
        json.dump(report, file, indent=4)
    print("Report saved to reports/report.json")