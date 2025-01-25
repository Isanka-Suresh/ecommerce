from product import Product

product = Product("laptop",36000,5)
print(product.get_details())

product.update_price(450000)
print(product.get_details())