import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mojito", 8.00, 6)

    def test_drink_has_name(self):
        self.assertEqual("Mojito", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(8.00, self.drink.price)