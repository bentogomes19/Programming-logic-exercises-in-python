#Make a program that receives the price of a product, calculates and displays the new price,
#knowing that the same has a 10% discount
#variables = product_price, new_price

product_price = float(input("Type the price of the product (US$): "))
new_price = (product_price * 0.10) + product_price
print(f'The new price of the product with a 10% discount is: US$ {new_price}')
