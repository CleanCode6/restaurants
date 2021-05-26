from page_maker import PageMaker
from curator import Curator
from db_connection import DBConnection
from model.restaurants import Restaurants, Parser
from typing import List

class Controller:
	def __init__(self):
		self.db = DBConnection()
		self.page_mk = PageMaker()
		self.db.connect_to_db()

	def restaurants_list_controller(self, request):
		search_list = Parser.to_list(self.db.get_restaurants())
		self.db.close_connection()
		curated_rests = Curator.curate_restaurant(search_list, request.args)
		return self.page_mk.make_restaurants_list_page(curated_rests, rests)

	def restaurant_controller(self, rest_id):
		rest = self.db.get_restaurant(rest_id)
		if rest is not None:
			rest = Parser.to_obj(rest)
		else:
			rest = {}
		self.db.close_connection()
		return self.page_mk.make_restaurant_page(rest)
