import unittest
from models import page, element, database, driver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        driver.connect()
        db = database
        db.connect()
        db.insert_page("Homepage","http://www.python.org",)
        db.insert_element("Search", "Search bar", "#id-search-field")
        db.insert_element("SearchButton", "Search bar button", ".search-button")

    def test_search_in_python_org(self):
        db.find_page("Homepage").goto()
        search = db.find_element("Search")
        search.input("pycon")
        button = db.find_element("SearchButton")
        button.click()
        assert "No results found." not in driver.page_source


    def tearDown(self):
        driver.disconnect()
        db.delete_page("Homepage")
        db.delete_page("Search")
        db.delete_page("SearchButton")
        db.disconnect()

if __name__ == "__main__":
    unittest.main()