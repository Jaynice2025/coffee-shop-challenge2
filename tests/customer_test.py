import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")
    
    def test_init(self):
        """Test that a Customer can be initialized with a name"""
        self.assertEqual(self.customer.name, "Alice")
    
    def test_name_getter(self):
        """Test that name getter returns the customer's name"""
        self.assertEqual(self.customer.name, "Alice")
    
    def test_name_setter_validation(self):
        """Test that name setter enforces type and length"""
        # Test valid name change
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        
        # Test invalid type
        with self.assertRaises(TypeError):
            self.customer.name = 123
        
        # Test too short
        with self.assertRaises(ValueError):
            self.customer.name = ""
        
        # Test too long
        with self.assertRaises(ValueError):
            self.customer.name = "ThisNameIsTooLong"
    
    def test_orders(self):
        """Test that orders() returns all orders for this customer"""
        # Initially should be empty
        self.assertEqual(len(self.customer.orders()), 0)
        
        # Create an order
        order = self.customer.create_order(self.coffee, 3.50)
        
        # Check that orders() returns the order
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertIn(order, self.customer.orders())
    
    def test_coffees(self):
        """Test that coffees() returns unique coffee instances"""
        # Initially should be empty
        self.assertEqual(len(self.customer.coffees()), 0)
        
        # Create orders
        self.customer.create_order(self.coffee, 3.50)
        self.customer.create_order(self.coffee, 3.75)  # Same coffee
        
        # Should only have one unique coffee
        coffees = self.customer.coffees()
        self.assertEqual(len(coffees), 1)
        self.assertIn(self.coffee, coffees)
        
        # Add another coffee
        another_coffee = Coffee("Latte")
        self.customer.create_order(another_coffee, 4.25)
        
        # Now should have two unique coffees
        coffees = self.customer.coffees()
        self.assertEqual(len(coffees), 2)
        self.assertIn(self.coffee, coffees)
        self.assertIn(another_coffee, coffees)
    
    def test_create_order(self):
        """Test that create_order creates a new Order"""
        order = self.customer.create_order(self.coffee, 3.50)
        
        # Check that the order has the right properties
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 3.50)
        
        # Check that the order is in the customer's orders
        self.assertIn(order, self.customer.orders())
        
        # Check that the order is in the coffee's orders
        self.assertIn(order, self.coffee.orders())
    
    def test_most_aficionado(self):
        """Test that most_aficionado returns the customer who's spent the most"""
        # Create another customer
        other_customer = Customer("Bob")
        
        # Alice spends $7.00 on Espresso
        self.customer.create_order(self.coffee, 3.50)
        self.customer.create_order(self.coffee, 3.50)
        
        # Bob spends $8.50 on Espresso
        other_customer.create_order(self.coffee, 4.25)
        other_customer.create_order(self.coffee, 4.25)
        
        # Bob should be the aficionado
        aficionado = Customer.most_aficionado(self.coffee)
        self.assertEqual(aficionado, other_customer)

if __name__ == "__main__":
    unittest.main()