import frappe
from frappe.utils import today, add_days

def assign_mandatory_courses(user, method):
    """Assign mandatory courses to newly created student users"""
    # if "LMS Student" not in frappe.get_roles(user.name):
    #     return

    # Fetch mandatory courses from Course Settings
    course_settings = frappe.get_single("Course Settings")
    if not course_settings or not course_settings.mandatory_courses:
        return

    for course in course_settings.mandatory_courses:
        course_name = course.course
        expire_days = course.expire or 30  # Default to 30 days if not set
        
        # Check if student is already enrolled
        if not frappe.db.exists("LMS Enrollment", {"course": course_name, "member": user.name}):
            enrollment = frappe.get_doc({
                "doctype": "LMS Enrollment",
                "member": user.name,
                "course": course_name,
                "deadline_date": add_days(today(), expire_days)
            })
            enrollment.insert()
            frappe.db.commit()
