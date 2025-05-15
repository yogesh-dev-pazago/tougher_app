# Copyright (c) 2025, Me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RideBooking(Document):
    def validate(self):
        if not self.rate:
            self.rate = frappe.db.get_single_value("Tougher Settings", "standard_rate")
        
        total_distance = 0
        print("Processing RideBooking:", self.name)
        
        # Use the correct child table name and convert string to float
        if hasattr(self, 'table_apcb') and self.table_apcb:
            for item in self.table_apcb:
                # Convert string distance to float before adding
                try:
                    item_distance = float(item.distance or 0)
                    total_distance += item_distance
                    print(f"Added distance: {item_distance}, Running total: {total_distance}")
                except (ValueError, TypeError):
                    frappe.msgprint(f"Invalid distance value in row: {item.idx}. Using 0.")
        else:
            print("No items found in table_apcb")
        
        # Convert rate to float as well to avoid type issues
        try:
            rate = float(self.rate or 0)
            self.total_amount = total_distance * rate
            print(f"Final calculation: {total_distance} * {rate} = {self.total_amount}")
        except (ValueError, TypeError):
            frappe.throw("Invalid rate value. Please enter a valid number.")