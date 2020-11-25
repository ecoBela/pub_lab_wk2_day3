import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mojito", 5.87)

    def test_drink_has_name(self):
        self.assertEqual("Mojito", self.drink.name)