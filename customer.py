from order import Order

class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = new_name

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod
    def most_aficionado(cls, coffee):
        highest = None
        highest_total = 0
        for customer in set(order.customer for order in coffee.orders()):
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > highest_total:
                highest_total = total
                highest = customer
        return highest
