import unittest
from models import driver, webpage, element, db

class SmokeTest(unittest.TestCase):

    def setUp(self):
        driver.connect()
        db.connect()
        self.page = db.page([None, "Homepage","http://www.python.org"]).insert()
        self.search_bar = db.element([None, "Search", "Search bar", "#id-search-field", self.page.id]).insert()
        self.search_button = db.element([None, "SearchButton", "Search bar button", ".search-button", self.page.id]).insert()

    def test_search_in_python_org(self):
        webpage.WebPage(db.select_page("Homepage")).goto()
        element.Element(db.select_element("Search")).input("pycon")
        element.Element(db.select_element("SearchButton")).click()
        assert "No results found." not in driver.driver.page_source


    def tearDown(self):
        driver.disconnect()
        self.page.delete()
        self.search_bar.delete()
        self.search_button.delete()
        db.disconnect()

if __name__ == "__main__":
    unittest.main()