import unittest
from models.db import database,page,select_page, element

class DbPageTests(unittest.TestCase):

    def setUp(self):
        database.connect()

    def test_insert_adds_one_row(self):
        cursor = database.connection.cursor()
        cursor.execute("SELECT Count(*) FROM pages")
        initial_count = cursor.fetchone()[0]
        page([None, "Homepage","http://www.python.org"]).insert()
        cursor.execute("SELECT Count(*) FROM pages")
        new_count = cursor.fetchone()[0]
        assert (initial_count + 1) == new_count

    def test_delete_removes_one_row(self):
        cursor = database.connection.cursor()
        webpage = page([None, "Homepage","http://www.python.org"]).insert()
        cursor.execute("SELECT Count(*) FROM pages")
        initial_count = cursor.fetchone()[0]
        webpage.delete()
        cursor.execute("SELECT Count(*) FROM pages")
        new_count = cursor.fetchone()[0]
        assert (initial_count - 1) == new_count

    def test_insert_only_updates_page_id(self):
        webpage = page([None, "Homepage","http://www.python.org"])
        assert webpage.id == None
        assert webpage.name == "Homepage"
        assert webpage.url == "http://www.python.org"
        webpage.insert()
        assert webpage.name == "Homepage" 
        assert webpage.url == "http://www.python.org"
        assert webpage.id != None

    def test_select_finds_record(self):
        inserted_page = page([None, "Homepage","http://www.python.org"]).insert()
        selected_page = select_page(inserted_page.name)
        assert inserted_page.name == selected_page.name 
        assert inserted_page.url == selected_page.url

    def test_select_by_page_id(self):
        webpage1 = page([None, "Google","http://www.google.com"]).insert()
        webpage2 = page([None, "Homepage","http://www.python.org"]).insert()

        element1 = element([None, "Search", "Search bar", "#id-search-field", webpage1.id]).insert()
        element2 = element([None, "Element", "Element", "#some-element", webpage1.id]).insert()
        element3 = element([None, "Search", "Search bar", "#id-search-field", webpage2.id]).insert()

        elements = webpage1.load_elements()
        assert elements[0].page_id == webpage1.id
        assert elements[1].name == "Element"
        assert elements[1].description == "Element"
        assert elements[1].selector == "#some-element"
        assert elements[1].page_id == webpage1.id
        assert len(elements) == 2

    def test_select_component_elements(self):
        webpage1 = page([None, "Google","http://www.google.com"]).insert()


    def tearDown(self):
        self.cursor.execute("TRUNCATE TABLE elements")
        database.connection.commit()
        self.cursor.execute("TRUNCATE TABLE components")
        database.connection.commit()
        self.cursor.execute("TRUNCATE TABLE pages")
        database.connection.commit()
        self.cursor.close()
        database.disconnect()

if __name__ == "__main__":
    unittest.main()