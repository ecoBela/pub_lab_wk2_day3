class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []

    def add_to_till(self, drink):
        return self.till + drink.price

    def check_age(self, customer_name):
        if customer_name.age >= 18:
            return True
        else:
            return False

    def assess_drunkenness(self, customer_name):
        if customer_name.drunkenness >= 12:
            return "Sorry, you're too drunk"
        else:
            return "You're boring and sober"