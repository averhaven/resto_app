from unittest import TestCase
from resto.restofind import Restaurant

class RestofindTest(TestCase):
    def test_create_restaurant(self):
        resto = Restaurant("Milo","Lindenstrase 4 Berlin")
        assert resto.name == "Milo"