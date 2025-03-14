app_name = "auto_backup"
app_title = "Auto Backup"
app_publisher = "Suleman Saeed"
app_description = "Take backup of the site"
app_email = "salmansaeed7272@gmail.com"
app_license = "mit"

# Apps
# ------------------

# scheduler_events = {
#     "cron": {
#         "*/1 * * * *": [
#             "auto_backup.api.backup_script.take_backup"
#         ]
#     }
# }

scheduler_events = {
    "cron": {
        "0 */2 * * *": [
            "auto_backup.api.backup_script.take_backup"
        ]
    }
}



# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "auto_backup",
# 		"logo": "/assets/auto_backup/logo.png",
# 		"title": "Auto Backup",
# 		"route": "/auto_backup",
# 		"has_permission": "auto_backup.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/auto_backup/css/auto_backup.css"
# app_include_js = "/assets/auto_backup/js/auto_backup.js"

# include js, css files in header of web template
# web_include_css = "/assets/auto_backup/css/auto_backup.css"
# web_include_js = "/assets/auto_backup/js/auto_backup.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "auto_backup/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "auto_backup/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "auto_backup.utils.jinja_methods",
# 	"filters": "auto_backup.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "auto_backup.install.before_install"
# after_install = "auto_backup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "auto_backup.uninstall.before_uninstall"
# after_uninstall = "auto_backup.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "auto_backup.utils.before_app_install"
# after_app_install = "auto_backup.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "auto_backup.utils.before_app_uninstall"
# after_app_uninstall = "auto_backup.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "auto_backup.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"auto_backup.tasks.all"
# 	],
# 	"daily": [
# 		"auto_backup.tasks.daily"
# 	],
# 	"hourly": [
# 		"auto_backup.tasks.hourly"
# 	],
# 	"weekly": [
# 		"auto_backup.tasks.weekly"
# 	],
# 	"monthly": [
# 		"auto_backup.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "auto_backup.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "auto_backup.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "auto_backup.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["auto_backup.utils.before_request"]
# after_request = ["auto_backup.utils.after_request"]

# Job Events
# ----------
# before_job = ["auto_backup.utils.before_job"]
# after_job = ["auto_backup.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"auto_backup.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

