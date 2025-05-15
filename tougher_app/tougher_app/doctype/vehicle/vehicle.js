// Copyright (c) 2025, Me and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
    refresh(frm) {

    },
    get_summary(frm) {
        frm.get_field("summary").$wrapper.append("<h1>Here is my summary</h1>")
    }
});
