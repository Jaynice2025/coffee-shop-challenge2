import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")
    
    def test_init(self):
        """Test that an Order can be initialized with customer, coffee, and price"""
        order = Order(self.customer, self.coffee, 3.50)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 3.50)
    
    def test_init_validation(self):
        """Test that Order.__init__ validates its parameters"""
        # Test invalid customer
        with self.assertRaises(TypeError):
            Order("not a customer", self.coffee, 3.50)
        
        # Test invalid coffee
        with self.assertRaises(TypeError):
            Order(self.customer, "not a coffee", 3.50)
        
        # Test invalid price type
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "not a number")
        
        # Test price too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.50)
        
        # Test price too high
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 15.00)
    
    def test_customer_getter(self):
        """Test that customer getter returns the customer instance"""
        order = Order(self.customer, self.coffee, 3.50)
        self.assertEqual(order.customer, self.customer)
    
    def test_coffee_getter(self):
        """Test that coffee getter returns the coffee instance"""
        order = Order(self.customer, self.coffee, 3.50)
        self.assertEqual(order.coffee, self.coffee)
    
    def test_price_getter(self):
        """Test that price getter returns the order price"""
        order = Order(self.customer, self.coffee, 3.50)
        self.assertEqual(order.price, 3.50)
    
    def test_price_immutability(self):
        """Test that order price is immutable"""
        order = Order(self.customer, self.coffee, 3.50)
        
        # Order doesn't have a price setter, so we check that price can't be changed directly
        with self.assertRaises(AttributeError):
            order.price = 4.00
    
    def test_add_to_customer_and_coffee(self):
        """Test that a new order is added to both customer and coffee"""
        order = Order(self.customer, self.coffee, 3.50)
        
        # Check that the order is in the customer's orders
        self.assertIn(order, self.customer.orders())
        
        # Check that the order is in the coffee's orders
        self.assertIn(order, self.coffee.orders())

if __name__ == "__main__":
    unittest.main()