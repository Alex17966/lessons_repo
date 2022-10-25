class RetailItem:
    def __init__(self, specification, quantity, price):
        self.specification = specification
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'Specification: {self.specification}, Quantity: {self.quantity}, Price: {self.price}'


item1 = RetailItem('Skirt', 10, 25)
item2 = RetailItem('Shoes', 15, 50)
item3 = RetailItem('T-shirt', 10, 25)


class CashRegister:
    def __init__(self, object1, object2, object3):
        self.object1 = object1
        self.object2 = object2
        self.object3 = object3
        self.list_ = []

    def purchase_item(self, product):
        self.list_.append(product)

    def get_total(self):                 #???????????????
        total_sum = 0
        for item in self.list_:
            total_sum += item

        print(f'The total sum of your items is {total_sum}')
        return total_sum

    def show_items(self):
        print('You have these items in your shopping basket:')
        for item in self.list_:
            print(item)

    def clear(self):
        self.list_.clear()
        print('Your shopping basket is empty')


cash_register = CashRegister(item1, item2, item3)
cash_register.purchase_item(item1)
cash_register.purchase_item(item1)
cash_register.purchase_item(item2)
# cash_register.get_total()
cash_register.show_items()
cash_register.clear()
