from . import __version__ as app_version

app_name = "task_tracker"
app_title = "Task Tracker"
app_publisher = "xsolutions"
app_description = "A custom app to track tasks"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "alaabadry1@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/task_tracker/css/task_tracker.css"
# app_include_js = "/assets/task_tracker/js/task_tracker.js"

# include js, css files in header of web template
# web_include_css = "/assets/task_tracker/css/task_tracker.css"
# web_include_js = "/assets/task_tracker/js/task_tracker.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "task_tracker/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "task_tracker.install.before_install"
# after_install = "task_tracker.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "task_tracker.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"task_tracker.tasks.all"
# 	],
# 	"daily": [
# 		"task_tracker.tasks.daily"
# 	],
# 	"hourly": [
# 		"task_tracker.tasks.hourly"
# 	],
# 	"weekly": [
# 		"task_tracker.tasks.weekly"
# 	]
# 	"monthly": [
# 		"task_tracker.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "task_tracker.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "task_tracker.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "task_tracker.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"task_tracker.auth.validate"
# ]
fixtures = ['Custom Field','Property Setter','Print Format','Role','Email Template']
doctype_js = {"Task" : "task_tracker/custom/js/task.js",
			"Project": "task_tracker/custom/js/project.js"}

doctype_list_js = {"Task" : "task_tracker/custom/js/task_list.js"}


doc_events = {
	"Project": {
		"validate": "task_tracker.custom.py.project.validate"
	},
	"Task": {
		"validate": "task_tracker.custom.py.task.validate",
		"on_trash": "task_tracker.custom.py.task.on_trash",
		"after_insert":"task_tracker.custom.py.task.after_insert"
	}
}
