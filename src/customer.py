class Customer:
    def __init__(self, name , wallet):
        self.name = name
        self.wallet = wallet
    
    def buy_drink(self, drink):
        # if self.wallet >= drink.price:
        return self.wallet - drink.price
                                                                                