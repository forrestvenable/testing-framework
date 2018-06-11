import unittest
from models import page, element, database, driver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        driver.connect()
        db = database.Database
        db.connect()
        db.insert_page("Homepage","http://www.python.org",)
        db.insert_element("Search", "Search bar", "#id-search-field")

    def test_search_in_python_org(self):
        db.find_page("Homepage").goto()
        elem = db.find_element("Search")
        elem.input("pycon")
        elem.input(Keys.RETURN)
        assert "No results found." not in self.driver.page_source


    def tearDown(self):
        driver.disconnect()
        db.delete_page("Homepage")
        db.delete_page("Search")
        db.disconnect()

if __name__ == "__main__":
    unittest.main()