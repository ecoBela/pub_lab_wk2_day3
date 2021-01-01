import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Skye", 50.00, 19)
        self.customer_2 = Customer("David", 25.00, 17)
        self.drink = Drink("Mojito", 8.00, 6)
        self.pub = Pub("Horse Whisperer", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Skye", self.customer_1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer_1.wallet)
    
    def test_customer_can_buy_drink(self):
        self.assertEqual(42, self.customer_1.buy_drink(self.drink))
        
    def test_customer_has_age(self):
        self.assertEqual(19, self.customer_1.age)

    def test_customer_drunkenness(self):
        self.assertEqual(6, self.customer_1.increase_drunkenness(self.drink))

