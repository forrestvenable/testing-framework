import unittest
from models.db import database,page,select_page

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


    def tearDown(self):
        cursor = database.connection.cursor()
        cursor.execute("TRUNCATE TABLE pages")
        database.connection.commit()
        database.disconnect()

if __name__ == "__main__":
    unittest.main()