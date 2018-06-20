import unittest
from models.db import database,page,select_page, element, component

class DbPageTests(unittest.TestCase):

    def setUp(self):
        database.connect()
        self.cursor = database.connection.cursor()

    def test_insert_adds_one_row(self):
        self.cursor.execute("SELECT Count(*) FROM pages")
        initial_count = self.cursor.fetchone()[0]
        page([None, "Homepage","http://www.python.org"]).insert()
        self.cursor.execute("SELECT Count(*) FROM pages")
        new_count = self.cursor.fetchone()[0]
        assert (initial_count + 1) == new_count

    def test_delete_removes_one_row(self):
        self.cursor = database.connection.cursor()
        webpage = page([None, "Homepage","http://www.python.org"]).insert()
        self.cursor.execute("SELECT Count(*) FROM pages")
        initial_count = self.cursor.fetchone()[0]
        webpage.delete()
        self.cursor.execute("SELECT Count(*) FROM pages")
        new_count = self.cursor.fetchone()[0]
        assert (initial_count - 1) == new_count

    def test_delete_removes_child_elements(self):
        self.cursor = database.connection.cursor()
        page1 = page([None, "Homepage","http://www.python.org"]).insert()
        elem1 = element([None, "Test", "Description", "#test-selector", page1.id, None]).insert()
        elem2 = element([None, "Test2", "Description2", "#test-selector2", None, None]).insert()
        self.cursor.execute("SELECT Count(*) FROM elements")
        initial_count = self.cursor.fetchone()[0]

        page1.delete()

        self.cursor.execute("SELECT Count(*) FROM elements")
        new_count = self.cursor.fetchone()[0]

        assert initial_count - 1 == new_count
        self.cursor.execute("SELECT COUNT(*) FROM elements WHERE name = %s AND description = %s AND selector = %s",
            (elem2.name,elem2.description,elem2.selector))
        not_deleted = self.cursor.fetchone()[0]
        assert not_deleted != 0

    def test_delete_removes_component_relationship(self):
        self.cursor = database.connection.cursor()
        page1 = page([None, "Homepage","http://www.python.org"]).insert()
        comp1 = component([None, "Test"]).insert()
        comp1.insert_into_page(page1)
        self.cursor.execute("SELECT Count(*) FROM components")
        initial_comp_count = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT Count(*) FROM pages_components")
        initial_rel_count = self.cursor.fetchone()[0]

        page1.delete()

        self.cursor.execute("SELECT Count(*) FROM components")
        new_comp_count = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT Count(*) FROM pages_components")
        new_rel_count = self.cursor.fetchone()[0]

        assert initial_comp_count == new_comp_count
        assert initial_rel_count - 1 == new_rel_count

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

    def test_load_elements_selects_page_elements(self):
        webpage1 = page([None, "Google","http://www.google.com"]).insert()
        webpage2 = page([None, "Homepage","http://www.python.org"]).insert()

        element1 = element([None, "Search", "Search bar", "#id-search-field", webpage1.id, None]).insert()
        element2 = element([None, "Element", "Element", "#some-element", webpage1.id, None]).insert()
        element3 = element([None, "Search", "Search bar", "#id-search-field", webpage2.id, None]).insert()

        elements = webpage1.load_elements()
        assert elements[0].page_id == webpage1.id
        assert elements[1].name == "Element"
        assert elements[1].description == "Element"
        assert elements[1].selector == "#some-element"
        assert elements[1].page_id == webpage1.id
        assert len(elements) == 2

    def test_load_elements_selects_child_component_elements(self):
        webpage1 = page([None, "Google","http://www.google.com"]).insert()
        comp1 = component([None, "Test"]).insert()
        comp2 = component([None, "Test2"]).insert()
        comp1.insert_into_page(webpage1)
        elem1 = element([None, "Test", "Description", "#test-selector", None, comp1.id]).insert()
        elem2 = element([None, "Test2", "Description2", "#test-selector2", None, None]).insert()

        webpage1.load_elements()
        assert(len(webpage1.elements) == 1)
        assert(webpage1.elements[0].id == elem1.id)
        assert(webpage1.elements[0].name == elem1.name)
        assert(webpage1.elements[0].description == elem1.description)
        assert(webpage1.elements[0].selector == elem1.selector)


    def test_select_component_elements(self):
        webpage1 = page([None, "Google","http://www.google.com"]).insert()


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