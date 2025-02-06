import hashlib
import frappe
import requests
from frappe import _
from frappe.core.doctype.user.user import User
from frappe.utils import cint, escape_html, random_string
from frappe.website.utils import is_signup_disabled
from lms.lms.utils import get_average_rating, get_country_code
from frappe.website.utils import cleanup_page_name
from frappe.model.naming import append_number_if_name_exists
from lms.widgets import Widgets


class CustomUser(User):

	def after_insert(self):
		super().after_insert()
		print("User created")
		print(self)