// Copyright (c) 2025, Me and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Make"] = {
	"filters": [
		{
			"fieldname": "my_filter",
			"fieldtype": "Link",
			"label": "My Filter",
			"options": "Vehicle",
		}
	]
};
