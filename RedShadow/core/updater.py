import subprocess
import logging

logging.basicConfig(filename="updater.log", level=logging.INFO)
logging.info("Starting updater module...")

def update():
    try:
        print("Checking for updates...")
        logging.info("Checking for updates...")

        result = subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True)

        if result.returncode == 0:
            print("Update successful.")
            print(result.stdout)
            logging.info("Update successful.")
            logging.info(result.stdout)
        else:
            print("Update failed.")
            print(result.stderr)
            logging.error("Update failed.")
            logging.error(result.stderr)
    except Exception as e:
        print(f"Error during update: {e}")
        logging.error(f"Error during update: {e}")

if __name__ == "__main__":
    update()