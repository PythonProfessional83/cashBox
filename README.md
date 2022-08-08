This program cashBox.py works with 2 classes: class RetailItem, class CashRegister.
Class RetaillItemm collects data about the product as desctiption, quantity, price.
price.
Class CashRegister has the following methods:

1. purchase_item() - acctepts object RetailItem as an argument and add it to the
   internal list using method purchaseItem() in the class CashRegister().
2. get_total() - returns total cost of all objects from the internal list in the class CashRegister.
3. show_items() - displays data of all objects RetailItem stored in internal list
   of class CashRegister and total price.
4. clear() - removes content of internal list of objects in the class CashRegister.

Class CashRegister allows the customer to choose many products, which he can buy.
When the user is ready to buy the products, program should display list of all choosen products
and their total price.

Action of cashBox.py

1. User get the list consisting of the product name and price.
1a. User chooses the product.
2. User enter quantity of choosen product.
3. Product name, quantity, price are passed to the object RetailItem.
4. RetailItem object is saved in the internal list of objects in the class CashRegister
   using method purchaseItem().
5. User is asked if he wants to buy next product or proceed to the basket to finalize
   the purchase.
6. If user chooses to finalize  diplay data of all objects RetailItem stored in internal list
   of class CashRegister.

output nr1:
Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 1


Enter quentity of the choosen product: 2

Shopping bascket: 2|| Current price: 300 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: y

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 2


Enter quentity of the choosen product: 2

Shopping bascket: 4|| Current price: 900 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: n

Products in the backet: 
------------------------

Product name: Tshirt
Quantity: 2
Price: 150

Product name: Jeans
Quantity: 2
Price: 300

Total price for all products is: : 900 PLN
======================================

Output nr 2:

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: ss
Please enter nr of the product to add it to the shopping bascket: 12
Please enter correct nr of the product to add it to the shopping bascket: 1


Enter quentity of the choosen product: 23000

Shopping bascket: 23000|| Current price: 3,450,000 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: y

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 2


Enter quentity of the choosen product: 43000

Shopping bascket: 66000|| Current price: 16,350,000 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: y

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 45
Please enter correct nr of the product to add it to the shopping bascket: 3


Enter quentity of the choosen product: 129000

Shopping bascket: 195000|| Current price: 74,400,000 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: y

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 4


Enter quentity of the choosen product: aa   
Enter quentity of the choosen product: w2
Enter quentity of the choosen product: 560000

Shopping bascket: 755000|| Current price: 214,400,000 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: y

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 5a
Please enter nr of the product to add it to the shopping bascket: 5


Enter quentity of the choosen product: r4
Enter quentity of the choosen product: 340000

Shopping bascket: 1095000|| Current price: 282,400,000 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: y

Hello! This is the list of the products with the prices.

1.Tshirt          : 150 zł
2.Jeans           : 300 zł
3.Jacket          : 450 zł
4.Normal trousers : 250 zł
5.Shorts          : 200 zł
6.Blouse          : 230 zł

Please enter nr of the product to add it to the shopping bascket: 6


Enter quentity of the choosen product: 45000

Shopping bascket: 1140000|| Current price: 292,750,000 PLN
==========================================
If you want to add more products press "y" or "any other mark" to finalize your purchase: n

Products in the backet: 
------------------------

Product name: Tshirt
Quantity: 23000
Price: 150

Product name: Jeans
Quantity: 43000
Price: 300

Product name: Jacket
Quantity: 129000
Price: 450

Product name: Normal trousers
Quantity: 560000
Price: 250

Product name: Shorts
Quantity: 340000
Price: 200

Product name: Blouse
Quantity: 45000
Price: 230

Total price for all products is: : 292,750,000 PLN
======================================

