class ElementManager:
	def __init__(driver):
		self.driver = driver

	def find_element(selector):
		driver = self.driver
		if(selector[0] == "#"):
			selenium_element = driver.find_element_by_id(selector[1:])
		else if(selector[0] == "."):
			selenium_element = driver.find_element_by_class(selector[1:])
		else:
			selenium_element = driver.find_element_by_name(selector)