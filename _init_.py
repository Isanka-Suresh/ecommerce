from product import Product
from customer import Customer

# product = Product("laptop",36000,5)
# print(product.get_details())

# product.update_price(450000)
# print(product.get_details())

# name = input("Enter product name: ")
# price = float(input("Enter product price: "))
# quantity = int(input("Enter product quantity: "))

# product1 = Product(name, price, quantity)
# print()
# print(product1.get_details())

name = input("Enter customer name: ")
address = input("Enter customer address: ")
contact = input("Enter customer contact: ")

customer = Customer(name, address, contact)
print()
print(customer.get_details())