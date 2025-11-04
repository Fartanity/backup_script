import os
import shutil
import json
from datetime import datetime

# Load config
with open("config.json", "r") as file:
    config = json.load(file)

SOURCE = config["source_folder"]
BACKUP = config["backup_folder"]
LOG_FILE = "logs/backup_log.txt"

# Create backup folder with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_path = os.path.join(BACKUP, f"backup_{timestamp}")

try:
    # Copy files
    shutil.copytree(SOURCE, backup_path)
    print(f"✅ Backup completed successfully! Files copied to: {backup_path}")

    # Log success
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] SUCCESS: Backup created at {backup_path}\n")

except Exception as e:
    print(f"❌ Backup failed: {e}")
    # Log failure
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] ERROR: {str(e)}\n")
