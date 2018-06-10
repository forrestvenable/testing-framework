class Page:
	def __init__(name, url, driver):
		this.name = name
		this.url = url
		this.driver = driver

	def goto:
		this.driver.get(this.url)

	def title:
		return this.driver.title