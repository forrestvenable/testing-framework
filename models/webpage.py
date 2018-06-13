from . import driver

class WebPage:
	def __init__(self, db_page):
		self.name = db_page.name
		self.url = db_page.url
		self.db_page = db_page

	def goto(self):
		driver.driver.get(self.url)