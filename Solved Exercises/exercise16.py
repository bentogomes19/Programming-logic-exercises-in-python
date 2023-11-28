#Make a program that receives:
# 1 - The bought product code, supposing that the typing of the product code is always validate, like
# integer numbers between 1 and 10
# 2 - The weight of the product in kilograms
# 3 - The  origin country code, supposing that the typing of the code will be always validate, like integer numbers
#between 1 and 3
#       Here the tables:
#  Origin country code          Tax         Product code           Price by gram
#       1                       0%              1 and 4                 US$ 0.12
#       2                       15%             5 and 7                 US$ 0.19
#       3                       25%             8 and 10                US$ 0.22
#
# Calculate and displays:
#   The weight of product converted in grams
#   The product's total price
#   The value of tax, knowing that it collected about the product's total price and depends the origin country
#   The total value and product price plus tax

product_code = int(input("Type the product code: "))
product_weight_kg = float(input("Type the product weight (Kg): "))
country_code = int(input("Type the origin country code: "))
convert_g = product_weight_kg * 1000


if product_code >= 1 and product_code <= 4:
    gram_price = 0.12
    print(f"the price by gram is US$ 0.12")
    print(f"The weight of the product in grams will be: {convert_g}g")
    product_price = gram_price * convert_g
    print(f'You will pay for the product: US$ {product_price}')
    
elif product_code >= 5 and product_code <=7:
    gram_price = 0.19
    print(f'The price by gram is US$ 0.19')
    print(f'The weight of the product in grams will be: {convert_g}g')
    product_price = gram_price * convert_g
    print(f'You will pay for the product: US$ {product_price}')
    
elif product_code >= 8 and product_code <= 10:
    gram_price = 0.22
    print(f'The price by gram is US$ 0.22')
    print(f'The weight of the product in grams will be: {convert_g}g')
    product_price = gram_price * convert_g
    print(f'You will pay for the product: US$ {product_price}')
else:
    print('INVALID CODE!')

if country_code == 1:
    tax = 0 * product_price
    total_value = product_price + tax
    print(f'Product price: US$ {product_price} | tax = U$ {tax} | total value: US$ {total_value}')
elif country_code == 2:
    tax = 0.15 * product_price
    total_value = product_price + tax
    print(f'Product price: US$ {product_price} | tax = U$ {tax} | total value: US$ {total_value}')
elif country_code == 3:
    tax = 0.25 * product_price
    total_value = product_price + tax
    print(f'Product price: US$ {product_price} | tax = U$ {tax} | total value: US$ {total_value}')
else:
    print('INVALID CODE!')
    


