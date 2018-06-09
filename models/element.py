class Element:
	def __init__(selenium_element):
		this.selenium_element = selenium_element
		pass

	def input(string):
		elem = this.selenium_element
		assert self.is_displayed()
		elem.send_keys(string)

	def is_displayed():
		elem = this.selenium_element
		return elem.displayed
