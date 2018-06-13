from . import database

class Page:
	def __init__(self, row):
		self.id = row[0]
		self.name = row[1]
		self.url = row[2]

	def insert(self):
		cursor = database.connection.cursor()
		cursor.execute("INSERT INTO pages (name, url) VALUES (%s, %s) RETURNING id", 
			(self.name, self.url))
		self.id = cursor.fetchone()[0]
		database.connection.commit()	
		cursor.close()
		return self

	def delete(self):
		cursor = database.connection.cursor()
		cursor.execute("DELETE FROM pages WHERE id = %s",
			(self.id,))
		database.connection.commit()	
		cursor.close()

def select(name):
	cursor = database.connection.cursor()
	cursor.execute("SELECT * FROM pages WHERE name = %s LIMIT 1",
		(name,))
	result = cursor.fetchone()
	cursor.close()
	return Page(result)

