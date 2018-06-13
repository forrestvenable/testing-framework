from . import driver

class WebPage:
	def __init__(self, db_page):
		self.name = db_page.name
		self.url = db_page.url
		self.db_page = db_page
		self.elements = self.db_page.elements

	def goto(self):
		driver.driver.get(self.url)

	def reload_elements(self):
		self.db_page.load_elements()
		self.elements = self.db_page.elements