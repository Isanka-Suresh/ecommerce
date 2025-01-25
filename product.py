class Product:
    def _init_(self, name ,price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_details(self):
        return f"{self.name} - ${self.price} - {self.quantity}"
    
    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def _str_(self):
        return f"{self.name} - ${self.price} - {self.quantity}"
    
    

# product1 = Product("apple", 1.99, 10)
# print(product1.get_details())
# product1.update_price(2.99)
# product1.update_quantity(20)
# print(product1)