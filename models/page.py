class Page:
	def __init__(self, name, url, driver):
		self.name = name
		self.url = url
		self.driver = driver

	def goto(self):
		self.driver.get(self.url)