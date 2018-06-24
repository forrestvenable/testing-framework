from . import database, element

class Page:
	def __init__(self, row):
		self.id = row[0]
		self.name = row[1]
		self.url = row[2]
		self.elements = []

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
		cursor.execute("DELETE FROM elements WHERE component_id IN (SELECT DISTINCT component_id FROM pages_components WHERE page_id = %s)",
			(self.id,))
		cursor.execute("DELETE FROM elements WHERE page_id = %s",
			(self.id,))
		cursor.execute("DELETE FROM pages_components WHERE page_id = %s",
			(self.id,))		
		cursor.execute("DELETE FROM pages WHERE id = %s",
			(self.id,))
		database.connection.commit()	
		cursor.close()

	def load_elements(self):
		cursor = database.connection.cursor()
		cursor.execute("SELECT * FROM elements WHERE page_id = %s",
			(self.id,))
		self.elements = []
		while (1):
			row = cursor.fetchone()
			if(row):
				self.elements.append(element.Element(row))
			else:
				break

 		cursor.execute("SELECT * FROM elements WHERE component_id IN (SELECT DISTINCT component_id FROM pages_components WHERE page_id = %s)",
 			(self.id,))
		while (1):
			row = cursor.fetchone()
			if(row):
				self.elements.append(element.Element(row))
			else:
				break

		return self.elements

	def to_json(self):
        return json.dumps(self.__dict__)

def select(name):
	cursor = database.connection.cursor()
	cursor.execute("SELECT * FROM pages WHERE name = %s LIMIT 1",
		(name,))
	result = cursor.fetchone()
	cursor.close()
	return Page(result)

