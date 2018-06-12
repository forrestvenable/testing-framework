import psycopg2
from . import element, webpage

class Database:
	def __init__(self):
		self.connection = None

	def connect(self):
		self.connection = psycopg2.connect("dbname='testing_framework' user='testing_framework' host='localhost' password='password'")

	def disconnect(self):
		self.connection.close()

	def insert_element(self, element):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO elements (name, description, selector) VALUES (%s, %s, %s)", 
			(element.name, element.description, element.selector))
		self.connection.commit()
		cursor.close()

	def insert_page(self, page):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO pages (name, url) VALUES (%s, %s)", 
			(page.name, page.url))
		self.connection.commit()	
		cursor.close()

	def select_element(self, name):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM elements WHERE name = %s LIMIT 1",
			(name,))
		results = cursor.fetchone()
		cursor.close()
		return element.Element(results[1], results[2], results[3])

	def select_page(self, name):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM pages WHERE name = %s LIMIT 1",
			(name,))
		results = cursor.fetchone()
		cursor.close()
		return webpage.WebPage(results[1], results[2])

	def delete_element(self, name):
		cursor = self.connection.cursor()
		cursor.execute("DELETE FROM elements WHERE name = %s",
			(name,))
		self.connection.commit()
		cursor.close()

	def delete_page(self, name):
		cursor = self.connection.cursor()
		cursor.execute("DELETE FROM pages WHERE name = %s",
			(name,))
		self.connection.commit()	
		cursor.close()

database = Database()