import pymysql
from model.restaurants import Restaurants

class DBConnection:
	def connect_to_db(self):
		self.DB = pymysql.connect(
		    user='cau', 
		    passwd='kG6byywEExRr', 
		    host='3.35.49.232', 
		    db='Restaurants', 
		    charset='utf8'
		)

	def get_restaurants(self):
		cursor = self.DB.cursor(pymysql.cursors.DictCursor)
		QUERY = 'SELECT * FROM Restaurants;'
		cursor.execute(QUERY)
		result = cursor.fetchall()
		return result

	def get_restaurant(self, restaurant_id):
		cursor = self.DB.cursor(pymysql.cursors.DictCursor)
		QUERY = f"SELECT * FROM Restaurants WHERE restaurant_id ='f{restaurant_id};'"
		cursor.execute(QUERY)
		result = cursor.fetchall()
		return result

	def close_connection(self):
		self.DB.close()
