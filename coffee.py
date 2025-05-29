class Coffee:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name   

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise AttributeError("Coffee cannot be changed after initialization.")
        if isinstance(name, str) and  len(name) >=3: 
            self._name = name
        else:
            raise ValueError("Name must be at least 3 characters.")
    
coffee_name = Coffee("Latte")
print(coffee_name.name)

coffee_name.name = "Espresso"

