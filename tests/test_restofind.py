from unittest import TestCase
from resto.restofind import Restaurant, recommend_resto

class RestofindTest(TestCase):
    def test_create_restaurant(self):
        resto = Restaurant("Milo","lindenstrase",4,10829,"Germany")
        assert resto.address.postal_code == 10829
    
    def test_recommend_resto(self):
        suggested_resto = recommend_resto(10829)
        assert suggested_resto.address.postal_code == 10829