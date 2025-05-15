# Copyright (c) 2025, Me and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []  
	columns = [
		{
			"fieldname": "make",
			"fieldtype": "Data",
			"label": "Make"
		},
		{
			"fieldname": "total_revenue",
			"fieldtype": "Currency",
			"label": "Total Revenue",
			"options": "AED",
		}
	]
	data = frappe.get_all(
		"Ride Booking", 
	    fields=["SUM(total_amount) AS total_revenue", "vehicle.make"],
		filters= {"docstatus": 1} ,
		group_by="make")
	charts = {
		"data": {
			"labels": [x.make for x in data],
			"datasets": [
				{
				"name": "Total Revenue",
				"values": [x.total_revenue for x in data]
			}
			],
		},
		"type": "pie"
	}
	return columns, data, "Message Summary", charts
