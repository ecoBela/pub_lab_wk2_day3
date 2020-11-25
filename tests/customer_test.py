import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Skye", 50.00)
        self.drink = Drink("Mojito", 8.00)

    def test_customer_has_name(self):
        self.assertEqual("Skye", self.customer.name)

    def test_customer_can_buy_drink(self):
        self.assertEqual(42, self.customer.buy_drink(self.drink))