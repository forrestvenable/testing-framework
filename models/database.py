import pyscopg2
from . import element, page

class Database:
	connection = None
	db = None

	def connect():
		connection = psycopg2.connect("dbname='testing_framework' user='testing_framework' host='localhost:5432' password='password'")
		db = connection.curser

	def disconnect():
		connection.close()
		db = None

	def insert_element(element):
		db.execute("INSERT INTO elements (name, description, selector) VALUES (%s, %s, %s)", 
			(element.name, element.description, element.selector))

	def insert_page(page):
		db.execute("INSERT INTO pages (name, url) VALUES (%s, %s)", 
			(page.name, page.url))		

	def select_element(name):
		results = db.execute("SELECT * FROM elements WHERE name = %s LIMIT 1",
			(name))
		return element.Element(results[0].name, results[0].description, results[0].selector)

	def select_page(name):
		results = db.execute("SELECT * FROM pages WHERE name = %s LIMIT 1",
			(name))
		return page.Page(results[0].name, results[0].url)

	def delete_element(name):
		db.execute("DELETE FROM elements WHERE name = %s",
			(name))

	def delete_page(name):
		db.execute("DELETE FROM pages WHERE name = %s",
			(name))		
