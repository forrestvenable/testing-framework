import unittest
from models.db import database,element,select_element

class DbPageTests(unittest.TestCase):

    def setUp(self):
        database.connect()

    def test_insert_adds_one_row(self):
        cursor = database.connection.cursor()
        cursor.execute("SELECT Count(*) FROM elements")
        initial_count = cursor.fetchone()[0]
        element([None, "Search", "Search bar", "#id-search-field", None]).insert()
        cursor.execute("SELECT Count(*) FROM elements")
        new_count = cursor.fetchone()[0]
        assert (initial_count + 1) == new_count

    def test_delete_removes_one_row(self):
        cursor = database.connection.cursor()
        webelement = element([None, "Search", "Search bar", "#id-search-field", None]).insert()
        cursor.execute("SELECT Count(*) FROM elements")
        initial_count = cursor.fetchone()[0]
        webelement.delete()
        cursor.execute("SELECT Count(*) FROM elements")
        new_count = cursor.fetchone()[0]
        assert (initial_count - 1) == new_count

    def test_insert_only_updates_element_id(self):
        webelement = element([None, "Search", "Search bar", "#id-search-field", None])
        assert webelement.id == None
        assert webelement.name == "Search"
        assert webelement.description == "Search bar"
        assert webelement.selector == "#id-search-field"
        webelement.insert()
        assert webelement.id != None
        assert webelement.name == "Search"
        assert webelement.description == "Search bar"
        assert webelement.selector == "#id-search-field"

    def test_select_finds_record(self):
        inserted_element = element([None, "Search", "Search bar", "#id-search-field", None]).insert()
        selected_element = select_element(inserted_element.name)
        assert inserted_element.name == selected_element.name 
        assert inserted_element.description == selected_element.description
        assert inserted_element.selector == selected_element.selector


    def tearDown(self):
        cursor = database.connection.cursor()
        cursor.execute("TRUNCATE TABLE elements")
        database.connection.commit()
        database.disconnect()

if __name__ == "__main__":
    unittest.main()