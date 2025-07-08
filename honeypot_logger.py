import time
import os

LOG_FILE = "honeypot_access.log"
SECRET_FILE = ".env"

def log_access(user):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.asctime()}: {user} accessed the secret file\n")

def display_secret():
    if os.path.exists(SECRET_FILE):
        with open(SECRET_FILE) as sf:
            secret = sf.read()
        print("Loaded secret:\n")
        print(secret)
        log_access(os.getenv("USER", "unknown"))
    else:
        print("Secret file not found.")

if __name__ == "__main__":
    display_secret()
