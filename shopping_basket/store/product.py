import csv
from decimal import Decimal

class  NoSuchProductError(Exception):
    pass

class ProductStore():

    def __init__(self,items):
        self.items=items

    def read_csv_file(self):
        with open(self.items,'r') as csvfile:
            csvreader = csv.reader(csvfile)
            product_list = []
            for row in csvreader:
                product_list.append((row[0], Decimal(row[1])))
            return product_list

    def show_available_product(self):
        product_list=self.read_csv_file()
        print('Available Product and price :')
        for i in product_list:
            print(i)

    def get_product_price(self, product_name):
        product_list=self.read_csv_file()
        #print(product_list)
        '''Return the price corresponding with the passed product_name.'''
        product_price = next((prod[1] for prod in product_list if prod[0] == product_name), None)
        if product_price is None:
            raise NoSuchProductError('No such product "{product_name}" in this store.'.format(product_name=product_name))
        else:
            return product_price


