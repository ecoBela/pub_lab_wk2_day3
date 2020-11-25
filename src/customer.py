class Customer:
    def __init__(self, name , wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
    
    def buy_drink(self, drink):
        # if self.wallet >= drink.price:
        return self.wallet - drink.price

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alco_level
        return self.drunkenness