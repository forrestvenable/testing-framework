from selenium import webdriver

driver = None

def connect
	driver = webdriver.Firefox()

def disconnect
	driver.close
	driver = None