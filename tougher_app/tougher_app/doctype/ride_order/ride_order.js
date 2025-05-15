// Copyright (c) 2025, Me and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if(frm.doc.status === "NEW") {
        frm.add_custom_button("Accept", () => {
            frappe.show_alert("Ride Booking Accepted");

            frm.set_value("status", "ACCEPTED");
            frm.save();
        } , "Actions");

        frm.add_custom_button("Reject", () => {
            frappe.show_alert("Ride Booking Rejected");

            frm.set_value("status", "REJECTED");
            frm.save();
        } , "Actions");
    }
  },
});

