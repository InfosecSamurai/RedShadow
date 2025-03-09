import os
import logging

def setup():
    # Set up logging
    logging.basicConfig(filename="setup.log", level=logging.INFO)
    logging.info("Starting RedShadow setup...")

    print("Setting up RedShadow...")

    try:
        # Ensure the reports directory exists
        if not os.path.exists("reports"):
            os.makedirs("reports")
            logging.info("Created directory: reports")

        # Ensure the logs directory exists
        if not os.path.exists("logs"):
            os.makedirs("logs")
            logging.info("Created directory: logs")

        # Ensure the templates directory exists
        if not os.path.exists("templates"):
            os.makedirs("templates")
            logging.info("Created directory: templates")

        # Ensure the script has execution permissions
        if os.path.exists("redshadow.py"):
            os.system("chmod +x redshadow.py")
            logging.info("Set execution permissions for redshadow.py")
        else:
            logging.warning("redshadow.py not found. Skipping permission change.")

        # Initialize the database
        if os.path.exists("core/database.py"):
            os.system("python3 core/database.py")
            logging.info("Initialized the database.")
        else:
            logging.warning("core/database.py not found. Skipping database initialization.")

        print("Setup complete.")
        logging.info("RedShadow setup completed successfully.")
    except Exception as e:
        print(f"Error during setup: {e}")
        logging.error(f"Error during setup: {e}")

if __name__ == "__main__":
    setup()