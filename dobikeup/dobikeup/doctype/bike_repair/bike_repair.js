// Copyright (c) 2019, Lewin Villar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bike Repair', {
	refresh: frm => {
		frm.add_fetch("messenger", "bike", "bike");
		frm.add_fetch("messenger", "frame_number", "frame_number");
	}
});
