import json
import datetime
import os

def run():
    findings = []
    
    while True:
        finding = input("Enter finding (or type 'done' to finish): ").strip()
        if finding.lower() == "done":
            break
        findings.append(finding)

    report = {
        "date": str(datetime.datetime.now()),
        "findings": findings
    }

    if not os.path.exists("reports"):
        os.makedirs("reports")

    report_path = "reports/report.json"
    with open(report_path, "w") as file:
        json.dump(report, file, indent=4)

    print(f"Report saved to {report_path}")
