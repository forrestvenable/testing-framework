import unittest
from models import db

class DbPageTests(unittest.TestCase):

    def setUp(self):
        db.connect()

    def insert_adds_one_row(self):
        cursor = database.connection.cursor()
        cursor.execute("SELECT Count(*) FROM pages")
        initial_count = cursor.fetchone()[0]
        self.page = db.page([None, "Homepage","http://www.python.org"]).insert()
        cursor.execute("SELECT Count(*) FROM pages")
        new_count = cursor.fetchone()[0]
        assert (initial_count + 1) == new_count

    def delete_removes_one_row(self):
        cursor = database.connection.cursor()
        self.page = db.page([None, "Homepage","http://www.python.org"]).insert()
        cursor.execute("SELECT Count(*) FROM pages")
        initial_count = cursor.fetchone()[0]
        self.page.delete()
        cursor.execute("SELECT Count(*) FROM pages")
        new_count = cursor.fetchone()[0]
        assert (initial_count - 1) == new_count

    def insert_only_updates_page_id(self):
        self.page = db.page([None, "Homepage","http://www.python.org"])
        assert self.page.id == None && self.page.name == "Homepage" && self.page.url == "http://www.python.org"
        self.page.insert()
        assert self.page.name == "Homepage" && self.page.url == "http://www.python.org"
        assert self.page.id != None

    def select_finds_record(self):
        self.page = db.page([None, "Homepage","http://www.python.org"]).insert()
        inserted_page = self.page
        selected_page = db.select(self.page.name)
        assert inserted_page.name == selected_page.name && inserted_page.url == selected_page.url


    def tearDown(self):
        driver.disconnect()
        self.page.delete()
        db.disconnect()

if __name__ == "__main__":
    unittest.main()