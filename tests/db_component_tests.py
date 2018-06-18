import db

class DbComponentTests(unittest.TestCase):
	def setup(self):
        database.connect()
        self.cursor = database.connection.cursor()

	def test_insert_creates_row(self):
		self.cursor.execute("SELECT Count(*) FROM components")
        initial_count = self.cursor.fetchone()[0]

        component([None, "Testing"]).insert()

        self.cursor.execute("SELECT Count(*) FROM components")
        new_count = self.cursor.fetchone()[0]
        assert (initial_count + 1) == new_count

    def test_delete_removes_row(self):
        comp = component([None, "Testing"]).insert()

		self.cursor.execute("SELECT Count(*) FROM components")
        initial_count = self.cursor.fetchone()[0]
        comp.delete()
        self.cursor.execute("SELECT Count(*) FROM components")
        new_count = self.cursor.fetchone()[0]
        assert (initial_count - 1) == new_count

    def test_delete_removes_child_elements(self):
        comp = component([None, "Testing"]).insert()
        ele1 = element([None, "Search", "Search bar", "#id-search-field", None, comp.id]).insert()
        ele2 = element([None, "Test", "Search bar", "#id-search-field", None, None]).insert()
        self.cursor("SELECT Count(*) FROM elements")
        old_count = self.cursor.fetchone()[0]

        comp.delete()

        self.cursor("SELECT Count(*) FROM elements")
        new_count = self.cursor.fetchone()[0]

        assert new_count + 1 == old_count

        self.cursor("SELECT COUNT(*) FROM elements WHERE name = 'Search'")
        no_rows = self.cursor.fetchone()[0]
        assert no_rows == 0

        self.cursor("SELECT COUNT(*) FROM elements WHERE name = 'Test'")
        rows = self.cursor.fetchone()[0]
        assert rows != 0

    def test_insert_into_page_works(self):
    	comp1 = component([None, "Test1"]).insert()
        page1 = page([None, "Test1","http://www.python.org"]).insert()
        
        self.cursor("SELECT COUNT(*) FROM pages_components WHERE component_id = %s AND page_id = %s",
        	(comp1.id, page1.id))
        initial_rows = self.cursor.fetchone()[0]        

        comp1.insert_into_page(page1)

        self.cursor("SELECT COUNT(*) FROM pages_components WHERE component_id = %s AND page_id = %s",
        	(comp1.id, page1.id))
        new_rows = self.cursor.fetchone()[0]

        assert initial_rows + 1 == new_rows

    def test_load_pages_works(self):
    	comp1 = component([None, "Test1"]).insert()
        page1 = page([None, "Test1","http://www.google.com"]).insert()
        page2 = page([None, "Test2","http://www.python.org"]).insert()
        comp1.insert_into_page(page1)

        comp1.load_pages()

        assert len(comp1.pages) == 1
        assert comp1.pages[0].name == page1.name
        assert comp1.pages[0].url == page1.url

    def test_load_elements_loads_correct_elements(self):
    	comp1 = component([None, "Test1"]).insert()
        comp2 = component([None, "Test2"]).insert()

        element1 = element([None, "Search", "Search bar", "#id-search-field", None, comp1.id]).insert()
        element2 = element([None, "Element", "Element", "#some-element", None, comp1.id]).insert()
        element3 = element([None, "Search", "Search bar", "#id-search-field", None, comp2.id]).insert()

        elements = comp1.load_elements()

        assert elements[0].page_id == webpage1.id
        assert elements[1].name == "Element"
        assert elements[1].description == "Element"
        assert elements[1].selector == "#some-element"
        assert elements[1].page_id == webpage1.id

        assert len(elements) == 2

    def tearDown(self):
        self.cursor.execute("TRUNCATE TABLE elements")
        database.connection.commit()
        self.cursor.execute("TRUNCATE TABLE pages_components")
        database.connection.commit()
        self.cursor.execute("TRUNCATE TABLE components")
        database.connection.commit()
        self.cursor.execute("TRUNCATE TABLE pages")
        database.connection.commit()
        self.cursor.close()
        database.disconnect()

if __name__ == "__main__":
    unittest.main()