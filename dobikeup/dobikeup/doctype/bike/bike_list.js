frappe.listview_settings['Bike'] = {
	"add_fields": ["status"],
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