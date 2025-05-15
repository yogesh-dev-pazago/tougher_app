import frappe

@frappe.whitelist(allow_guest=True)
def get_emojis():
    return "👍",

def throw_emoji(doc, event):
    frappe.throw("👎")

def throw_emoji_final():
    pass

def get_query_conditions_for_vehicle(user):
    return "title = 'Something Model, 2022'"
