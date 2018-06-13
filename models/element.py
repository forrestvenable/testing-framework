from . import driver

class Element:
	def __init__(self, db_element):
		self.name = db_element.name
		self.description = db_element.description
		self.selector = db_element.selector
		self._selenium_element = None
		self.db_element = None

	def input(self, string):
		self._lazy_find()
		elem = self._selenium_element
		assert self.is_displayed
		elem.clear()
		elem.send_keys(string)

	def click(self):
		self._lazy_find()
		assert self.is_displayed
		self._selenium_element.click()

	def is_displayed(self):
		self._lazy_find()
		return self._selenium_element.displayed

	def _lazy_find(self):
		if(not self._selenium_element):
			self._selenium_element = driver.driver.find_element_by_css_selector(self.selector)


