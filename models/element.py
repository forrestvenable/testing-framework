class Element:
	def __init__(name, description, selector, driver):
		this.name = name
		this.description = description
		this.selector = selector
		this.driver = driver
		this._selenium_element = None

	def input(string):
		elem = _lazy_load()
		assert this.is_displayed()
		elem.send_keys(string)

	def click:
		elem = _lazy_load()
		assert this.is_displayed()
		elem.click()

	def is_displayed:
		elem = _lazy_load()
		elem = this.selenium_element
		return elem.displayed

	def _lazy_load:
		elem = this._selenium_element
		if(!elem):
			driver = this.driver
			if(this.selector[0] == "."):
				elem = driver.find_element_by_class(this.selector[1:])
			else if(this.selector[0] == "#"):
				elem = driver.find_element_by_id(this.selector[1:])
			else:
				elem = driver.find_element_by_name(this.selector)
		return elem


