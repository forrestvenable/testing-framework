import unittest
import element
import page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = page.Page("Homepage","http://www.python.org", self.driver)
        self.elem = element.Element("Search", "Search bar", "q")

    def test_search_in_python_org(self):
        self.page.goto()
        self.assertIn("Python", self.page.title())
        elem = driver.find_element_by_name("q")
        elem.input("pycon")
        elem.input(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()