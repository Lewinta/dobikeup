# -*- coding: utf-8 -*-
# Copyright (c) 2019, Lewin Villar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ScheduleCheckup(Document):
	def get_schedule_template(self):
		self.details = []

		if not self.template:
			return

		if not frappe.db.exists("Schedule Checkup Template", self.template):
			return

		doc = frappe.get_doc("Schedule Checkup Template", self.template)

		for detail in doc.details:
			self.append("details", {
				"description": detail.get('description')
			})
