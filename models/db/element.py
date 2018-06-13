from . import database

class Element:
	def __init__(self, row):
		self.id = row[0]
		self.name = row[1]
		self.description = row[2]
		self.selector = row[3]
		self.page_id = row[4]

	def insert(self):
		cursor = database.connection.cursor()
		cursor.execute("INSERT INTO elements (name, description, selector, page_id) VALUES (%s, %s, %s, %s) RETURNING id", 
			(self.name, self.description, self.selector, self.page_id))
		database.connection.commit()
		self.id = cursor.fetchone()[0]
		cursor.close()
		return self

	def delete(self):
		cursor = database.connection.cursor()
		cursor.execute("DELETE FROM elements WHERE id = %s",
			(self.id,))
		database.connection.commit()
		cursor.close()

def select(name):
	cursor = database.connection.cursor()
	cursor.execute("SELECT * FROM elements WHERE name = %s LIMIT 1",
		(name,))
	result = cursor.fetchone()
	cursor.close()
	return Element(result)

def select_by_page_id(page_id)
	cursor = database.connection.cursor()
	cursor.execute("SELECT * FROM elements WHERE page_id = %s",
		(page_id,))
	results = []
	while (row = cursor.fetchone()):
		results.append(Element(row))

	return results