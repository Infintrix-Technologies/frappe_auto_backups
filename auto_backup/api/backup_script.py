import subprocess
import os
import time
from pathlib import Path
import frappe

def get_backup_settings():
    settings = frappe.get_single("Backup Setting")
    return {
        "backup_retention_days": settings.backup_retention_days,
        "backup_time": settings.backup_time,
    }


# def take_backup():
#     backup_path = Path.home() / "frappe-backup/sites/localhost/private/backups"

#     print("Starting backup process...")

#     deletion_time = 120

#     # Run the backup command
#     command = "bench backup --with-files --compress"
#     process = subprocess.run(command, shell=True, capture_output=True, text=True)


#     # Delete backup files older than 5 minutes
#     now = time.time()
#     for file in backup_path.glob("*"):
#         if file.is_file() and now - file.stat().st_mtime > deletion_time:  # 604800 seconds = 7 days
#             os.remove(file)
#             print(f"Deleted old backup: {file}")


#     if process.returncode == 0:
#         print("Backup completed successfully.")
#     else:
#         print(f"Backup failed: {process.stderr}")







import os
import time
import subprocess
from pathlib import Path








def take_backup():

    settings = get_backup_settings()
    backup_retention_days = settings["backup_retention_days"]
    backup_time = settings["backup_time"]

    backup_path = Path.home() / "frappe-backup/sites/localhost/private/backups"
    deletion_time = int(backup_retention_days) 
    min_backup_interval = int(backup_time)  

    print("Starting backup process...")

    # Find the most recent backup file
    latest_backup = None
    latest_time = 0

    for file in backup_path.glob("*"):
        if file.is_file():
            file_mtime = file.stat().st_mtime
            if file_mtime > latest_time:
                latest_time = file_mtime
                latest_backup = file

    now = time.time()

    # Check if the last backup was taken within the min_backup_interval
    if latest_backup and (now - latest_time) < min_backup_interval:
        print("Skipping backup. Last backup was taken recently.")
        return

    # Run the backup command
    command = "bench backup --with-files --compress"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)

    if process.returncode == 0:
        print("Backup completed successfully.")
    else:
        print(f"Backup failed: {process.stderr}")

    # Delete old backup files (older than 2 minutes)
    for file in backup_path.glob("*"):
        if file.is_file() and (now - file.stat().st_mtime) > deletion_time:
            os.remove(file)
            print(f"Deleted old backup: {file}")





