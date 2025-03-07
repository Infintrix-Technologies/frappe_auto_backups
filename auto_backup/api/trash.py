import subprocess
import os
import time
from pathlib import Path

def take_backup():
    # site = "localhost"

    print(f"Starting backup")

    command = "bench backup --with-files --compress"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)

    if process.returncode == 0:
        print("Backup completed successfully.")
    else:
        print(f"Backup failed: {process.stderr}")










def take_backup():
    backup_path = Path.home() / "frappe-backup/sites/localhost/private/backups"

    print("Starting backup process...")

    deletion_time = 120

    # Run the backup command
    command = "bench backup --with-files --compress"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)


    # Delete backup files older than 5 minutes
    now = time.time()
    for file in backup_path.glob("*"):
        if file.is_file() and now - file.stat().st_mtime > deletion_time:  # 604800 seconds = 7 days
            os.remove(file)
            print(f"Deleted old backup: {file}")


    if process.returncode == 0:
        print("Backup completed successfully.")
    else:
        print(f"Backup failed: {process.stderr}")








def time_to_seconds(time_str):
    """Convert time string (HH:MM:SS or MM:SS) to seconds."""
    parts = list(map(int, time_str.split(":")))
    if len(parts) == 3:  # HH:MM:SS
        hours, minutes, seconds = parts
    elif len(parts) == 2:  # MM:SS
        hours, minutes, seconds = 0, parts[0], parts[1]
    elif len(parts) == 1:  # SS
        hours, minutes, seconds = 0, 0, parts[0]
    else:
        raise ValueError("Invalid time format")

    return hours * 3600 + minutes * 60 + seconds
