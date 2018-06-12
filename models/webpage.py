from . import driver

class WebPage:
	def __init__(self, name, url):
		self.name = name
		self.url = url

	def goto(self):
		driver.driver.get(self.url)