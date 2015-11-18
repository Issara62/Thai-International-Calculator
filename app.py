__author__ = 'Singtothong'

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty

import CurrencyFunction

class ThaiInterCalc(App):
    total_bill = 0
    receipt = []
    satay_options = ['Chicken Satay', 'Beef Satay', 'Mixed Satay']
    spinner_satay = ListProperty()
    all_items_spinner = ListProperty()

    order_number = 1
    def build(self):
        self.title = 'Thai International Calculator'
        self.root = Builder.load_file('gui.kv')

        # Set satay options
        self.spinner_satay = self.satay_options
        self.all_items_spinner = self.receipt

        return self.root

    def add_total(self, amount, food):
        # Set total amount
        float(amount)
        self.total_bill = self.total_bill + amount
        total = 'The total bill is: ' + CurrencyFunction.format_currency(self.total_bill)
        self.root.ids.Total_bill.text = str(total)

        #Set spinner of menu items
        menu_item = (str(self.order_number) + ' . ' + food + ' - ' + CurrencyFunction.format_currency(amount))
        print(menu_item)
        self.receipt.append(menu_item)
        self.all_items_spinner = self.receipt
        self.order_number = self.order_number + 1

        self.number_of_items(1)

    def add_purchase_items(self, string):
        text = ''
        text2 = text + string
        text2.split('-')
        print(text2)
        self.root.ids.Total_items.multiline = True
        self.root.ids.Total_items.text = str(text2)

    def number_of_items(self, handle):

        numer = str(self.order_number + handle)
        value = 'Number of items: ' + numer
        self.root.ids.Number_of_items.text = str(value)

        pass

    def delete_item(self, order):
        pass










ThaiInterCalc().run()