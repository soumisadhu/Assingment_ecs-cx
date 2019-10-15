import os
import unittest
from decimal import Decimal

from cart import Cart, CartItem
from product import ProductStore
from offers import  BuyGetOffer, PercentageDiscountOffer

productDetail=ProductStore('test_products.csv')
class CartTest(unittest.TestCase):

    def test_add_one_items(self):
        cart = Cart()
        cart.add('Biscuits',2)
        self.assertEqual(cart.get_total(), 2.4)

    def test_add_two_items(self):
        cart = Cart()
        cart.add('Biscuits',2)
        cart.add('Baked Beans',3)
        self.assertEqual(cart.get_total(), 5.37)

    def test_add_two_same_items(self):
        cart = Cart()
        cart.add('Biscuits',2)
        cart.add('Biscuits',2)
        self.assertEqual(cart.get_total(), 4.8)

    def test_add_items_no_quantity(self):
        #if no quanity is given default value is 1
        cart = Cart()
        cart.add('Biscuits')
        cart.add('Baked Beans')
        self.assertEqual(cart.get_total(), 2.19)

    def test_duplicate_items_no_quantity(self):
        #if no quanity is given default value is 1 for two duplicate item
        cart = Cart()
        cart.add('Biscuits')
        cart.add('Biscuits')
        self.assertEqual(cart.get_total(), 2.4)

    def test_buy_get_offer(self):
        #Calculate the price while there is buy 3 get 2 offer with quantity 3
        cart = Cart()
        cartitem=cart.add('Biscuits',3)
        multibuy_apples=BuyGetOffer('Biscuits', 3, 2)
        self.assertEqual(multibuy_apples.calculate_line_total(
            cartitem), Decimal('3.6'))

    def test_buy_get_offer(self):
        #Calculate the price while there is buy 3 get 2 offer with quantity 6
        cart = Cart()
        cartitem=cart.add('Biscuits',6)
        multibuy_apples=BuyGetOffer('Biscuits', 3, 2)
        self.assertEqual(
            cart.get_total(offers=[multibuy_apples]), Decimal(4.8))

    def test_percentage_discount_offer(self):
        #calculate the price while there is 25% offer in product
        cart = Cart()
        cartitem=cart.add('Baked Beans',4)
        percentdiscount = PercentageDiscountOffer('Baked Beans',0.15)
        self.assertEqual(
            cart.get_total(offers=[percentdiscount]), Decimal(3.366))

    def combined_offer(self):

        cart = Cart()
        cart.add('Biscuits',8)
        cart.add('Baked Beans',4)
        multibuy_apples = BuyGetOffer('Biscuits', 5, 2)
        percentdiscount = PercentageDiscountOffer('Baked Beans',0.15)
        self.assertEqual(
            cart.get_total(offers=[multibuy_apples,percentdiscount]), Decimal(10.566))






