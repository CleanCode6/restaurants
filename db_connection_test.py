import unittest
from db_connection import DBConnection

class DBConnectionTest(unittest.TestCase):
	def test_get_restaurant_list(self):
		db = DBConnection()
		db.connect_to_db()
		result = db.get_restaurants()
		print(result)

	def test_get_restaurants(self):
		db = DBConnection()
		db.connect_to_db()
		rest_id = 1
		result = db.get_restaurant(rest_id)
		print(result)

if __name__ == '__main__':
    unittest.main()