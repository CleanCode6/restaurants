from flask import render_template

class PageMaker:
	def make_restaurant_page(self, restaurant):
		return render_template("restaurant_page.html", result=restaurant)

	def make_restaurants_list_page(self, curated, restaurants):
		return render_template("restaurants_list_page.html", result=[curated, restaurants])
