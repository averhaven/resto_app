import requests
from dataclasses import dataclass
from resto.secret_key import get_secret_key


"""creates the class restaurant with a name and address"""
@dataclass
class Restaurant:
    name: str
    address: str

#TODO errorhandling
"""input is a postal code. output is a location. the location is given by calling the geocoding api"""
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

#TODO errorhandling
"""input is a location(lat + longitude). output 10 restaurants. calls nearbysearch api"""
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