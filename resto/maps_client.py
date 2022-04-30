import requests
import json
from flask import current_app
from resto.secret_key import get_secret_key

def get_maps_client():
    if current_app.env == "production":
        return GoogleMapsClient(get_secret_key())
    else:
        return TestMapsClient()

class MapsClient:
    def geocode(self, postal_code: str) -> dict:
        """returns the location based on postal code"""
    
    def nearby_search(self, location: dict) -> dict:
        """returns restaurants based on location"""

class GoogleMapsClient(MapsClient):
    def __init__(self, api_key):
        self.api_key = api_key

    def geocode(self, postal_code: str) -> dict:
        """returns the location based on postal code"""
        url = "https://maps.googleapis.com/maps/api/geocode/json?"
        params = {
            "components":"country:DE|postal_code:{}".format(postal_code),
            "key":self.api_key
        }
        response = requests.get(url, params=params)
        return response.json()
    
    def nearby_search(self, location: dict) -> dict:
        """returns restaurants based on location"""
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        params = {
            "location": "{},{}".format(location["lat"], location["lng"]),
            "radius":500,
            "type":"restaurant",
            "key":self.api_key
        }
        response = requests.get(url, params=params)
        return response.json()

class TestMapsClient(MapsClient):
    def geocode(self, postal_code: str) -> dict:
        """returns the location based on postal code"""
        return {'results': [{'address_components': [{'long_name': '10829', 'short_name': '10829', 'types': ['postal_code']}, {'long_name': 'Tempelhof-Schöneberg', 'short_name': 'Tempelhof-Schöneberg', 'types': ['political', 'sublocality', 'sublocality_level_1']}, {'long_name': 'Berlin', 'short_name': 'Berlin', 'types': ['locality', 'political']}, {'long_name': 'Kreisfreie Stadt Berlin', 'short_name': 'Kreisfreie Stadt Berlin', 'types': ['administrative_area_level_3', 'political']}, {'long_name': 'Berlin', 'short_name': 'BE', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Germany', 'short_name': 'DE', 'types': ['country', 'political']}], 'formatted_address': '10829 Berlin, Germany', 'geometry': {'bounds': {'northeast': {'lat': 52.4929736, 'lng': 13.3762297}, 'southwest': {'lat': 52.4662421, 'lng': 13.3452184}}, 'location': {'lat': 52.4803778, 'lng': 13.3597304}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 52.4929736, 'lng': 13.3762297}, 'southwest': {'lat': 52.4662421, 'lng': 13.3452184}}}, 'place_id': 'ChIJ84Wg_hRQqEcRINs9lUkgIRw', 'types': ['postal_code']}], 'status': 'OK'}
    
    def nearby_search(self, location: dict) -> dict:
        """returns restaurants based on location"""
        with open("tests/nearby_search_results.json","r") as fd:
            response = json.load(fd)
        return response