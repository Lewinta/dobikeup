// Copyright (c) 2019, Lewin Villar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Schedule Checkup', {
	refresh: function(frm) {

	},
	template: frm => {
		if (!frm.doc.template){
			frm.clear_table("details");
			frm.refresh_field("details")
			return
		}

		frm.call("get_schedule_template")
	}
});
