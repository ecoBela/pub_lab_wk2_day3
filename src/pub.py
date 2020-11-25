class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []

    def add_to_till(self, drink):
        return self.till + drink.price