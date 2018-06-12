from selenium import webdriver


driver = None

def connect():
	global driver
	driver = webdriver.Firefox()

def disconnect():
	global driver
	driver.close
	driver = None