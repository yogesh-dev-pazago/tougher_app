// Copyright (c) 2025, Me and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {

	},

    rate(frm , cdt , cdn) {
       frm.trigger("update_total_amount");
    },

    update_total_amount(frm) {
        let total_dist = 0;
        for( let item of frm.doc.table_apcb) {
            total_dist += item.distance;
        }
        const amount = total_dist * frm.doc.rate;
        frm.set_value("total_amount", amount);
    }
});


frappe.ui.form.on("Ride Booking Item", {
	refresh(frm) {

	},
    distance(frm , cdt , cdn) {
        frm.trigger("update_total_amount");
    },
    table_apcb_remove(frm) {
        frm.trigger("update_total_amount");
    }

});
