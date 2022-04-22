# first draft of the python code that recommends restaurant based on given postal code using api
import json
import requests
from flask import Blueprint, render_template, request, url_for, redirect, flash

bp = Blueprint("resto", __name__)

class Restaurant:
    def __init__(self, restaurant_name, restaurant_address):
        """creates the class restaurant with a name and address"""
        self.name = restaurant_name
        self.address = restaurant_address

def get_secret_key():
    with open("secrets_api.json", "r") as fd:
        data = json.load(fd)
    return data["SECRET_KEY"]

#input is a postal code. output is a location. the location is given by calling the geocoding api
def location_from_postal_code(postal_code):
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = {
        "components":"country:DE|postal_code:{}".format(postal_code),
        "key":get_secret_key()
    }
    response = requests.get(url, params=params)
    data = response.json()
    location = data["results"][0]["geometry"]["location"]
    return location

#input is a location(lat + longitude). output 10 restaurants. calls nearbysearch api
def resto_from_location(location):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    params = {
        "location": "{},{}".format(location["lat"], location["lng"]),
        "radius":500,
        "type":"restaurant",
        "key":get_secret_key()
    }
    response = requests.get(url, params=params)
    data = response.json()
    restaurant_data = data["results"][:10]
    return restaurant_data


def recommend_resto(postal_code):
    location = location_from_postal_code(postal_code)
    restaurant_data = resto_from_location(location)
    restaurants = convert_to_resto(restaurant_data)
    return restaurants


def convert_to_resto(restaurant_data):
    restaurants = []
    for r in restaurant_data:
        resto = Restaurant(r["name"], r["vicinity"])
        restaurants.append(resto)
    return restaurants


def validate_german_postal_code(postal_code):
    if len(postal_code) == 5 and postal_code.isdecimal():
        return True
    else:
        return False

@bp.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        postal_code = request.form['postal_code']
        if not validate_german_postal_code(postal_code):
            flash("This is not a valid postal code for germany")
        else:
            return redirect(url_for(".postal_code_search", postal_code=postal_code))
    return render_template("restofind.html")

@bp.route("/postalcode/<string:postal_code>")
def postal_code_search(postal_code):
    restaurants = recommend_resto(postal_code)
    return render_template("postal.html", restaurants=restaurants)