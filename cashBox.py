# cashBox.py
''' 
Please read Readme.md
This program cashBox.py works with 2 classes: class RetailItem, class CashRegister.
1. User get the list consisting of the product name and price.
2. User enter quantity of choosen product.
3. Product name, quantity, price are passed to the object RetailItem.
4. RetailItem object is saved in the internal list of objects on class CashRegister
   using method purchaseItem().
5. User is asked if he wants to buy next product or proceed to the basket to finalize
   the purchase.
6. If user chooses to finalize the purchase, list of all products and
   total price are displaied.
'''
# to create object ReatailItem
import retail
# to create object CashRegister
import cash
from simple_colors import *


def main():

    # initializer
    question = 'y'
    productsQty = 0

    while question.lower() == 'y':
        # display menu, choose product
        name, price = displayProducts()  # returns tuple (name, price)

        # current quantity of the choosed products
        quantit_y = quantity()  # returns quantity
        productsQty += quantit_y
        

        # product name, price, quantity are passed to the object RetailItem
        retailItem = retail.RetailItem(name, price, quantit_y)

        # creating object cashRegister
        cashRegister = cash.CashRegister()

        # Saving retailItem object in the internal list of objects in the class CashRegister
        cashRegister.purchaseItem(retailItem)
        
        # current price for all products in the current bascket = 
        # current condition of cash.Register.get_total() inside while loop
        currentPrice = cashRegister.get_total()

        print()
        # displaying current conditon of the shopping bascket
        print(f'Shopping bascket: {productsQty}|| Current price: {currentPrice:,} PLN')
        print((len('shopping bascket    current price         '))*'=')
        
        # asking the user if he wants to buy next product or proceed to 
        # the the shopping basket to finalize the purchase.
        question = input(red(
            'If you want to add more products press "y" or "any other mark" to finalize your purchase: ',['bold', 'underlined']))

        # if the user wants to add more products
        print()

    # display all purchased products
    pr = 'Products in the backet: '
    print(pr)
    print(len(pr)*'-')

    # creating list of objects
    listObject_s = cashRegister.listObjects()

    # iterate throught the list of objects and displaying condition of attributes of retailItem objects in the list
    # due to method __str__() in the retail.py
    for produ_ct in listObject_s:
        print(produ_ct)
    print()

    #clear list with all objects to get current total price, otherwicse total price will be diubled
    #
    cashRegister.clear()
    
    # display total price of all purchased products
    # totalPrice object is outside whe while loop, therfore gives total price, from the list saved
    # in the file list.dat
    #
    totalPrice = cashRegister.get_total()
    tot = 'Total price for all products is: '
    print(f'{tot}: {totalPrice:,} PLN')
    print((len(tot)+5)*'=')
    
    # clear internal list saved in the file list.dat
    cashRegister.clear()
    


def displayProducts():
    products = ['Tshirt', 'Jeans', 'Jacket',
                'Normal trousers', 'Shorts', 'Blouse']
    prices = [150, 300, 450, 250, 200, 230]

    print('Hello! This is the list of the products with the prices.')
    print()

    count = 0
    for product, price in zip(products, prices):
        count += 1
        print(f'{count}.{product:<16}: {price:,} zł')
    print()

    # to enter correct nr
    fla_g = True
    while fla_g:
        try:
            # choose the product
            productNr = int(
                input('Please enter nr of the product to add it to the shopping bascket: '))

            while productNr < 1 or productNr > 6:
                productNr = int(input(
                    'Please enter correct nr of the product to add it to the shopping bascket: '))

            # flag must be outside while loop
            fla_g = False

        except ValueError:
            pass

    # extracting product name
    productName = products[(productNr - 1)]
    # extracting product price
    productPrice = prices[(productNr-1)]

    print()
    return (productName, productPrice)


def quantity():
    print()

    # enter correct quantity
    fla_g = True
    while fla_g:
        try:
            qty = int(input('Enter quentity of the choosen product: '))
            fla_g = False
        except ValueError:
            pass

    return qty


main()
