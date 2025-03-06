import os

def setup():
    print("Setting up RedShadow...")

    # Ensure the reports directory exists
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Ensure the script has execution permissions
    os.system("chmod +x redshadow.py")

    print("Setup complete.")

if __name__ == "__main__":
    setup()
