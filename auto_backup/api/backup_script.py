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



def get_site_name():
    """Get the current site name dynamically from the sites directory, 
    removing 'hrms.' prefix if present"""
    
    sites_path = Path.home() / "frappe-bench/sites"
    
    for site in sites_path.iterdir():
        if site.is_dir() and (site / "site_config.json").exists(): 
            site_name = site.name
            return site_name.removeprefix("hrms.")  
    
    return None 




def take_backup():
    site_name = get_site_name()
    if not site_name:
        print("No valid Frappe site found!")
        return

    settings = get_backup_settings()
    backup_retention_days = int(settings["backup_retention_days"])
    backup_time = int(settings["backup_time"])

    backup_path = Path.home() / f"frappe-backup/sites/{site_name}/private/backups"
    deletion_time = backup_retention_days
    min_backup_interval = backup_time  

    print(f"Starting backup process for site: {site_name}")

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

    # Run the backup command for the detected site
    command = f"bench --site {site_name} backup --with-files --compress"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)

    if process.returncode == 0:
        print("Backup completed successfully.")
    else:
        print(f"Backup failed: {process.stderr}")

    # Delete old backup files
    for file in backup_path.glob("*"):
        if file.is_file() and (now - file.stat().st_mtime) > deletion_time:
            os.remove(file)
            print(f"Deleted old backup: {file}")


