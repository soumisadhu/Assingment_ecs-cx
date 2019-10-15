from store.product import ProductStore
from store.offers import BuyGetOffer
from store.offers import PercentageDiscountOffer

productDetail=ProductStore('products.csv')

class Cart(object):
    def __init__(self):
        self.items = []

    def add(self, item, quantity=1):
        cart_item=next((item for item in self.items if item.product == item), None)
        if cart_item is None:
            cart_item = CartItem(item, quantity)
            self.items.append(cart_item)
        else:
            cart_item.quantity += quantity
        return cart_item

    def get_total(self,offers=None):
        totals = []
        for item in self.items:
            line_total = item.get_line_total()

            if offers is not None:
                for offer in offers:
                    if offer.target_product == item.product:
                        offer_total = offer.calculate_line_total(
                            item, self)
                        if offer_total < line_total:
                            line_total = offer_total

            totals.append(line_total)
            final=float(sum(totals))
        print("subtotal:{}".format(final))
        return final

class CartItem(object):

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    def get_line_total(self):
        total = productDetail.get_product_price(self.product) * self.quantity
        print('total:{}'.format(total))
        return total

def main():

    a=Cart()
    productDetail.show_available_product()
    flag = 'y'
    while flag !='n':

        item=input('Enter item: ')
        quantity = int(input('Enter quantity: '))
        a.add(item,quantity)
        flag=input('Want to enter more items ? y/n: ')

    """Here types of offers are hardcoded"""
    multibuy_apples = BuyGetOffer('Biscuits', 5, 2)
    percentdiscount = PercentageDiscountOffer('Baked Beans',0.15)
    a.get_total(offers=[percentdiscount,multibuy_apples])


if __name__=='__main__':
    main()
