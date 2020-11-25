import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Skye", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("Skye", self.customer.name)