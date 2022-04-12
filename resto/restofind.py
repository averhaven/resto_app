# first draft of the python code that recommends restaurant based on given postal code
import json
from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("resto", __name__)

class Restaurant:
    def __init__(self, restaurant_name, street_name, street_number, postal_code, country):
        """creates the class restaurant with a name and address"""
        self.address = Address(
            street_name, street_number, postal_code, country)
        self.name = restaurant_name


class Address:
    def __init__(self, street_name, street_number, postal_code, country):
        """creates the class address using a street name, number, postal code and country"""
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country


def recommend_resto(postal_code):
    """input is a postal code. output is a restaurant in the area of the given postal code.
    the function first searches a restaurant in the dictionary"""
    with open("resto/restaurants.json", "r") as fd:
        data = json.load(fd)
    resto_list = convert_to_resto(data)
    result = find_postalcode_in_list(postal_code, resto_list)
    return result


def convert_to_resto(data):
    resto_list = []
    for r in data:
        resto = Restaurant(r["restaurantName"], r["streetName"],
                           r["streetNumber"], r["postalCode"], r["country"])
        resto_list.append(resto)
    return resto_list


def find_postalcode_in_list(postal_code, resto_list):
    resto_matching_postal = []
    for r in resto_list:
        if postal_code == r.address.postal_code:
            resto_matching_postal.append(r)
    return resto_matching_postal

@bp.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        postal_code = request.form['postal_code']
        return redirect(url_for(".postal_code_search", postal_code=postal_code))
    return render_template("restofind.html")

@bp.route("/postalcode/<string:postal_code>")
def postal_code_search(postal_code):
    restaurants = recommend_resto(postal_code)
    return render_template("postal.html", restaurants=restaurants)