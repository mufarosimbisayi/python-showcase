class Purchase():
	def __init__(self, purchase_dict):
		self.street = purchase_dict["street"]
		self.city = purchase_dict["city"]
		self.zip = purchase_dict["zip"]
		self.state = purchase_dict["state"]
		self.beds = int(purchase_dict["beds"])
		self.baths = int(purchase_dict["baths"])
		self.sq__ft = purchase_dict["sq__ft"]
		#self.residential = purchase_dict["Residential"]
		#self.scale_date = purchase_dict["scale_date"]
		self.price = float(purchase_dict["price"])
		self.latitude = purchase_dict["latitude"]
		self.longitude = purchase_dict["longitude"]
