# -*- coding: utf-8 -*-
# Copyright (c) 2019, Lewin Villar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BikeRepair(Document):
	def submit(self):
		self.create_stock_entry()

	def create_stock_entry(self):
		if not self.parts:
			return
		ste = frappe.new_doc("Stock Entry")
		ste.update({
			"purpose":"Material Issue",
			"from_warehouse": "Stores - DB",
			"to_warehouse": "Finished Goods - DB"
		})

		for row in self.parts:
			ste.append("items",{
				"item_code": row.item,
				"qty": row.qty,
			})

		ste.save()
		ste.submit()
