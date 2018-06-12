import unittest
from models import database, driver, webpage, element

class FirstTest(unittest.TestCase):

    def setUp(self):

        driver.connect()
        database.database.connect()
        database.database.insert_page(webpage.WebPage("Homepage","http://www.python.org"))
        database.database.insert_element(element.Element("Search", "Search bar", "#id-search-field"))
        database.database.insert_element(element.Element("SearchButton", "Search bar button", ".search-button"))

    def test_search_in_python_org(self):
        database.database.select_page("Homepage").goto()
        search = database.database.select_element("Search")
        search.input("pycon")
        button = database.database.select_element("SearchButton")
        button.click()
        assert "No results found." not in driver.driver.page_source


    def tearDown(self):
        driver.disconnect()
        database.database.delete_page("Homepage")
        database.database.delete_page("Search")
        database.database.delete_page("SearchButton")
        database.database.disconnect()

if __name__ == "__main__":
    unittest.main()