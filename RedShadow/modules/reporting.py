import json
import datetime
import os
import logging
from jinja2 import Environment, FileSystemLoader

def get_findings():
    findings = []
    while True:
        finding = input("Enter finding (or type 'done' to finish): ").strip()
        if finding.lower() == "done":
            break
        findings.append(finding)
    return findings

def generate_html_report(report, report_path):
    try:
        # Load the HTML template
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("report_template.html")

        # Render the template with report data
        html_content = template.render(report=report)

        # Save the HTML report
        with open(report_path, "w") as file:
            file.write(html_content)
        print(f"HTML report saved to {report_path}")
        logging.info(f"HTML report saved to {report_path}")
    except Exception as e:
        print(f"Error generating HTML report: {e}")
        logging.error(f"Error generating HTML report: {e}")

def run():
    logging.basicConfig(filename="reporting.log", level=logging.INFO)
    logging.info("Starting reporting module...")

    print("Generating report...")

    findings = get_findings()
    if not findings:
        print("No findings entered. Report generation aborted.")
        logging.warning("No findings entered. Report generation aborted.")
        return

    report = {
        "date": str(datetime.datetime.now()),
        "findings": findings
    }

    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        try:
            os.makedirs(reports_dir)
            logging.info(f"Created directory: {reports_dir}")
        except OSError as e:
            print(f"Error creating directory: {e}")
        logging.error(f"Error creating directory: {e}")
        return

# Generate JSON report
json_report_path = os.path.join(reports_dir, "report.json")
try:
    with open(json_report_path, "w") as file:
        json.dump(report, file, indent=4)
    print(f"JSON report saved to {json_report_path}")
    logging.info(f"JSON report saved to {json_report_path}")
except IOError as e:
    print(f"Error saving JSON report: {e}")
    logging.error(f"Error saving JSON report: {e}")

# Generate HTML report
html_report_path = os.path.join(reports_dir, "report.html")
generate_html_report(report, html_report_path)

print("Report generation complete.")
logging.info("Reporting module completed.")