import driver

class Page:
	def __init__(self, name, url):
		self.name = name
		self.url = url

	def goto(self):
		driver.get(self.url)