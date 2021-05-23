from page_maker import PageMaker
from curator import Curator
from db_connection import DBConnection
from distance_operator import DistanceOperator
from model.restaurants import Restaurants
from typing import List

class Controller:
	def __init__(self):
		self.db = DBConnection()
		self.page_mk = PageMaker()
		self.db.connect_to_db()

	def restaurants_list_controller(self, request):
		rests = self.db.get_restaurants()
		self.db.close_connection()
		curated_rests = Curator.curate_restaurant(rests, request)
		return self.page_mk.make_restaurants_list_page(curated_rests, rests)

	def restaurant_controller(self, rest_id):
		rest = self.db.get_restaurant(rest_id)
		self.db.close_connection()
		return self.page_mk.make_restaurant_page(rest)
