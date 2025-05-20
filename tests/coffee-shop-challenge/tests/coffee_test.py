import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Espresso")
        self.customer = Customer("Alice")
    
    def test_init(self):
        """Test that a Coffee can be initialized with a name"""
        self.assertEqual(self.coffee.name, "Espresso")
        
        # Test name validation
        with self.assertRaises(TypeError):
            Coffee(123)  # Not a string
        
        with self.assertRaises(ValueError):
            Coffee("Ab")  # Too short
    
    def test_name_getter(self):
        """Test that name getter returns the coffee's name"""
        self.assertEqual(self.coffee.name, "Espresso")
    
    def test_name_immutability(self):
        """Test that coffee name is immutable"""
        # Coffee doesn't have a name setter, so we check that name can't be changed directly
        with self.assertRaises(AttributeError):
            self.coffee.name = "Latte"
    
    def test_orders(self):
        """Test that orders() returns all orders for this coffee"""
        # Initially should be empty
        self.assertEqual(len(self.coffee.orders()), 0)
        
        # Create an order
        order = self.customer.create_order(self.coffee, 3.50)
        
        # Check that orders() returns the order
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertIn(order, self.coffee.orders())
    
    def test_customers(self):
        """Test that customers() returns unique customer instances"""
        # Initially should be empty
        self.assertEqual(len(self.coffee.customers()), 0)
        
        # Create orders with the same customer
        self.customer.create_order(self.coffee, 3.50)
        self.customer.create_order(self.coffee, 3.75)
        
        # Should only have one unique customer
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 1)
        self.assertIn(self.customer, customers)
        
        # Add another customer
        another_customer = Customer("Bob")
        another_customer.create_order(self.coffee, 4.25)
        
        # Now should have two unique customers
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 2)
        self.assertIn(self.customer, customers)
        self.assertIn(another_customer, customers)
    
    def test_num_orders(self):
        """Test that num_orders returns the total count of orders"""
        # Initially should be 0
        self.assertEqual(self.coffee.num_orders(), 0)
        
        # Create orders
        self.customer.create_order(self.coffee, 3.50)
        self.customer.create_order(self.coffee, 3.75)
        
        # Should now be 2
        self.assertEqual(self.coffee.num_orders(), 2)
    
    def test_average_price(self):
        """Test that average_price returns the mean price"""
        # Initially should be 0
        self.assertEqual(self.coffee.average_price(), 0)
        
        # Create orders
        self.customer.create_order(self.coffee, 3.00)
        self.customer.create_order(self.coffee, 5.00)
        
        # Average should be 4.00
        self.assertEqual(self.coffee.average_price(), 4.00)

if __name__ == "__main__":
    unittest.main()