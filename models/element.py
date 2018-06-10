class Element:
	def __init__(name, description, selector, driver):
		this.name = name
		this.description = description
		this.selector = selector
		this.driver = driver
		this._selenium_element = None

	def input(string):
		elem = _lazy_find()
		assert this.is_displayed()
		elem.send_keys(string)

	def click:
		elem = _lazy_find()
		assert this.is_displayed()
		elem.click()

	def is_displayed:
		elem = _lazy_find()
		elem = this.selenium_element
		return elem.displayed

	def _lazy_find:
		elem = this._selenium_element
		if(!elem):
			driver = this.driver
			elem = driver.find_element_by_css_selector(this.selector)
		return elem


