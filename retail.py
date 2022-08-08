# retail.py
'''
Please read Readme.md
Class RetaillItemm collects data about the product as desctiption, quantity, price.
price.
'''


class RetailItem:
    def __init__(self, description, price, quantity):
        self.description = description
        self.price = price
        self.quantity = quantity
        

    # creates getters
    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    # returns all string data about the product
    def __str__(self):
        return '\nProduct name: ' + self.description + \
               '\nQuantity: ' + str(self.quantity) + \
               '\nPrice: ' + str(self.price)
