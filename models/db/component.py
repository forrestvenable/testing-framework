from . import database, element

class Component:
	def __init__(self, row):
		self.id = row[0]
		self.name = row[1]
		self.elements = []

	def insert(self):
		cursor = database.connection.cursor()
		cursor.execute("INSERT INTO components (name) VALUES (%s) RETURNING id", 
			(self.name,))
		self.id = cursor.fetchone()[0]
		database.connection.commit()	
		cursor.close()
		return self

	def delete(self):
		cursor = database.connection.cursor()
		cursor.execute("DELETE FROM elements WHERE component_id = %s",
			(self.id,))
		cursor.execute("DELETE FROM components WHERE id = %s",
			(self.id,))
		database.connection.commit()	
		cursor.close()

	def load_elements(self):
		cursor = database.connection.cursor()
		cursor.execute("SELECT * FROM elements WHERE component_id = %s",
			(self.id,))
		results = []
		while (1):
			row = cursor.fetchone()
			if(row):
				results.append(element.Element(row))
			else:
				break

		self.elements = results
		return self.elements