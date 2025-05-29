class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def orders(self):
        return self._orders.copy()
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def add_order(self, order):
        self._orders.append(order)


    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
        


class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def orders(self):
        return self._orders.copy()
    
    def customers(self):
        return list({order.customer for order in self._orders})
    
    def add_order(self, order):
        self._orders.append(order)

    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        num_orders = len(self._orders)
        average_price = total_price / num_orders
        return average_price


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        customer.add_order(self)
        coffee.add_order(self)


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self,"_price"):
            raise AttributeError("Price cannot be changed after initialized.")
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float and between 1.0 and 10.0")

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance.")
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance.")
        self._coffee = coffee
        
# order = Order("Jerome", "Espresso", 10.0)
# print(order.price)

customer = Customer("Jerome")
customer1 = Customer("Chauncey")
customer121 = Customer("Jaseh")


latte = Coffee("Latte")
espresso = Coffee("Espresso")
plain = Coffee("Plain")
plain = Coffee("Plain")
dark_coffee = Coffee("Dark Coffee")
fancy = Coffee("Fancy")




Order(customer, latte, 10.0)
Order(customer, espresso, 5.0)
Order(customer, plain, 9.0)
Order(customer, plain, 9.0)
Order(customer1, dark_coffee, 2.0)
Order(customer121, fancy, 2.2)

print(f"{customer.name}'s Orders:")
for o in customer.orders():
    print(f"Order: {o.coffee.name} for ${o.price}")


print(f"Unique coffees ordered by {customer.name}:")
for coffee in customer.coffees():
    print(f"{coffee.name}")


print(len(customer.orders()))

print("Coffee Popularity")
print(f"Latte ordered {latte.num_orders()} times")
print(f"Espresso ordered {espresso.num_orders()} times")
print(f"Plain ordered {plain.num_orders()} times")
print(f"Dark Coffee ordered {dark_coffee.num_orders()} times")




americano = Coffee("Americano")
customer1 = Customer("Alice")
customer2 = Customer("Bob")

Order(customer1, americano, 3.5)
Order(customer2, americano, 4.5)

print(americano.average_price())  
print(Coffee("Americano").average_price())  




    