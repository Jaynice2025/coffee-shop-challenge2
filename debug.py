"""
Debug script to test the coffee shop domain model.
Run this file to see the classes in action.
"""

from customer import Customer
from coffee import Coffee
# Order is imported implicitly when needed

def main():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    
    print(f"Created customers: {alice.name}, {bob.name}, and {charlie.name}")
    
    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    print(f"Created coffees: {espresso.name}, {latte.name}, and {cappuccino.name}")
    
    # Create orders
    print("\nCreating orders...")
    
    # Alice likes espresso
    alice.create_order(espresso, 3.25)
    alice.create_order(espresso, 3.25)
    
    # Bob likes lattes
    bob.create_order(latte, 4.50)
    bob.create_order(latte, 4.50)
    
    # Charlie tries everything
    charlie.create_order(espresso, 3.25)
    charlie.create_order(latte, 4.50)
    charlie.create_order(cappuccino, 5.00)
    
    # Display customer orders
    for customer in [alice, bob, charlie]:
        print(f"\n{customer.name}'s orders:")
        for order in customer.orders():
            print(f"  {order.coffee.name}: ${order.price:.2f}")
    
    # Display coffee stats
    for coffee in [espresso, latte, cappuccino]:
        print(f"\n{coffee.name} stats:")
        print(f"  Number of orders: {coffee.num_orders()}")
        print(f"  Average price: ${coffee.average_price():.2f}")
        print(f"  Customers: {', '.join(customer.name for customer in coffee.customers())}")
    
    # Find aficionados
    print("\nCoffee aficionados:")
    for coffee in [espresso, latte, cappuccino]:
        aficionado = Customer.most_aficionado(coffee)
        if aficionado:
            print(f"  {coffee.name}: {aficionado.name}")
        else:
            print(f"  {coffee.name}: None")

if __name__ == "__main__":
    main()