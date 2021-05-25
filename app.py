from flask import Flask, redirect, request, url_for
from controller import Controller

app = Flask(__name__)

@app.route('/')
def default_route():
	return redirect(url_for('restaurants_list_route'))

@app.route('/restaurants')
def restaurants_list_route():
	cont = Controller()
	return cont.restaurants_list_controller(request)

@app.route('/restaurants/<rest_id>')
def restaurant_route(rest_id):
	cont = Controller()
	return cont.restaurant_controller(rest_id)
