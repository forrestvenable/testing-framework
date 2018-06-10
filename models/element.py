class Element:
	def __init__(self, name, description, selector, driver):
		self.name = name
		self.description = description
		self.selector = selector
		self.driver = driver
		self._selenium_element = None

	def input(self, string):
		elem = self._lazy_find()
		assert self.is_displayed
		elem.send_keys(string)

	def click(self):
		elem = self._lazy_find()
		assert self.is_displayed
		elem.click()

	def is_displayed(self):
		elem = self._lazy_find()
		return elem.displayed

	def _lazy_find(self):
		elem = self._selenium_element
		if(not elem):
			driver = self.driver
			elem = driver.find_element_by_css_selector(self.selector)
		return elem


