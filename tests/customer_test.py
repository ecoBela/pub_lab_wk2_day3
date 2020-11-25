import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Skye", 50.00, 19)
        self.customer_2 = Customer("David", 25.00, 17)
        self.drink = Drink("Mojito", 8.00)

    def test_customer_has_name(self):
        self.assertEqual("Skye", self.customer_1.name)

    def test_customer_can_buy_drink(self):
        self.assertEqual(42, self.customer_1.buy_drink(self.drink))

    def test_customer_has_age(self):
        self.assertEqual(19, self.customer_1.age)

