from store.product import ProductStore
from decimal import Decimal
import csv
productDetail=ProductStore('products.csv')

class BuyGetOffer():

    def __init__(self, target_product, charge_for_quantity, free_quantity, *args, **kwargs):
        self.charge_for_quantity = charge_for_quantity
        self.free_quantity = free_quantity
        self.target_product=target_product

    def calculate_line_total(self, cart_item, *args):
        print("Offer is:Buy {} {} Get {} free ".format(self.target_product,self.charge_for_quantity,self.free_quantity))
        bundles, remainder = divmod(
            cart_item.quantity, self.charge_for_quantity + self.free_quantity)
        if remainder > self.charge_for_quantity:
            bundles += 1
            remainder = 0
        charge_quantity = (bundles * self.charge_for_quantity) + remainder
        return productDetail.get_product_price(cart_item.product) * charge_quantity

class PercentageDiscountOffer():
    def __init__(self,target_product,discount_amount):
        self.target_product=target_product
        self.discount_amount=discount_amount

    def calculate_line_total(self,cart_item,*args):
        percentage=int(self.discount_amount*100)
        print("Offer is: {} {}% Discount ".format(self.target_product,percentage))
        total_price=float(cart_item.quantity*productDetail.get_product_price(cart_item.product))
        discounted_price=(total_price-(self.discount_amount*total_price))
        return Decimal(discounted_price)

