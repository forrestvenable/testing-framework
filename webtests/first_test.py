import unittest
from models import driver, webpage, element, db

class FirstTest(unittest.TestCase):

    def setUp(self):
        driver.connect()
        db.database.connect()
        self.page = db.page.Page([None, "Homepage","http://www.python.org"]).insert()
        self.search_bar = db.element.Element([None, "Search", "Search bar", "#id-search-field", self.page.id]).insert()
        self.search_button = db.element.Element([None, "SearchButton", "Search bar button", ".search-button", self.page.id]).insert()

    def test_search_in_python_org(self):
        webpage.WebPage(db.page.select("Homepage")).goto()
        element.Element(db.element.select("Search")).input("pycon")
        element.Element(db.element.select("SearchButton")).click()
        assert "No results found." not in driver.driver.page_source


    def tearDown(self):
        driver.disconnect()
        self.page.delete()
        self.search_bar.delete()
        self.search_button.delete()
        db.database.disconnect()

if __name__ == "__main__":
    unittest.main()