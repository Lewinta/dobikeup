frappe.listview_settings['Messenger'] = {
	"add_fields": ["status", "docstatus"],
	"onload": (listview) => {
		
	},
	"get_indicator": (doc) => {
		if(doc.status === "OK") {
			return ["OK", "green", "status,=,OK"]
		} else if (doc.status === "NOT OK") {
			return ["NOT OK", "red", "status,=,NOT OK"]
		} 
	}
}