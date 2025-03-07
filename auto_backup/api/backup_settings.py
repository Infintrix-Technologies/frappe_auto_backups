
import frappe


def get_backup_settings():
    settings = frappe.get_single("Backup Setting")
    return {
        "backup_retention_days": settings.backup_retention_days,
        "backup_time": settings.backup_time,
    }
