# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Dobikeup",
			"color": "blue",
			"icon": "fa fa-bicycle",
			"type": "module",
			"label": _("Dobikeup")
		},
		{
			"module_name": "Item",
			"_doctype": "Item",
			"color": "#f39c12",
			"icon": "fa fa-wrench",
			"type": "link",
			"link": "List/Item/List",
			"label": _("Item")
		},
		{
			"module_name": "Messenger",
			"_doctype": "Messenger",
			"color": "#ac77dc",
			"icon": "fa fa-user",
			"type": "link",
			"link": "List/Messenger/List",
			"label": _("Messenger")
		},
		{
			"module_name": "Schedule Checkup",
			"_doctype": "Schedule Checkup",
			"color": "#5890d6",
			"icon": "fa fa-calendar",
			"type": "link",
			"link": "List/Schedule Checkup/List",
			"label": _("Schedule Checkup")
		}
	]
