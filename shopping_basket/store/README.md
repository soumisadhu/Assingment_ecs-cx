Pre-requisite:
install unittest either from reuirements.txt or using pip install unittest.
------------------------------------
To run Shopping_cart program:

1.cd /shopping_basket/store
2.python cart.py

Available Product and price :
('Baked Beans', Decimal('0.99'))
('Biscuits', Decimal('1.20'))
('Sardines', Decimal('1.89'))
('Shampoo (Small)', Decimal('2.00'))
('Shampoo (Medium)', Decimal('2.50'))
('Shampoo (Large)', Decimal('3.50'))
Enter item: Biscuits
Enter quantity: 8
Want to enter more items ? y/n: n
total:9.60
Offer is:Buy Biscuits 5 Get 2 free
subtotal:7.2

usecase 2:

Available Product and price :
('Baked Beans', Decimal('0.99'))
('Biscuits', Decimal('1.20'))
('Sardines', Decimal('1.89'))
('Shampoo (Small)', Decimal('2.00'))
('Shampoo (Medium)', Decimal('2.50'))
('Shampoo (Large)', Decimal('3.50'))
Enter item: Biscuits
Enter quantity: 8
Want to enter more items ? y/n: y
Enter item: Baked Beans
Enter quantity: 4
Want to enter more items ? y/n: n
total:9.60
Offer is:Buy Biscuits 5 Get 2 free
total:3.96
Offer is: Baked Beans 15% Discount
subtotal:10.566


N:B Note that offers are hardcodded in cart.py file.So if you want to change offer change in cart.py and run the program.
i.e
multibuy_apples = BuyGetOffer('Shampoo (Small)', 2, 1)

---------------------------------------------
To run unit test.

python tests.py
------------------------------------
