import os

def update():
    print("Checking for updates...")
    os.system("git pull origin main")
    print("Update complete.")

if __name__ == "__main__":
    update()