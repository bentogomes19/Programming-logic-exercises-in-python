#A SUPERMARKET WANTS TO READJUST THE PRICES OF ITS PRODUCTS USING THE FOLLOWING CRITERION: THE
#PRODUCT CAN HAVE ITS PRICE INCREASED OR DECREASED. FOR THE PRICE TO CHANGE, THE PRODUCT MUST 
#FULFILL AT LEAST ONE OF THE FOLLOWING REQUIREMENTS:
#
# AVERAGE MONTHLY SALES          CURRENT PRICE          % INCREASE     % DECREASE
#          <500                    <R$ 30,00                10             -
#     >=500 AND < 1.200     >= R$ 30,00 AND <R$ 80,00       15             -
#     >= 1.200                      >= R$ 80,00              -             20
# MAKE A PROGRAM THAT RECEIVES THE CURRENT PRICE AND THE AVERAGE MONTHLY SALE OF THE PRODUCT, CALCULATES AND DISPLAYS THE NEW PRICE


current_price = float(input("Type the current price of the product (US$): "))
average_monthly_sale = float(input("Type the average monthly sale of the product (US$): "))
if current_price < 30 and average_monthly_sale < 500:
    increase = current_price * 0.1
    new_price = current_price + increase
    print(f"The new price of the product is: US$ {new_price} | increase: US$ {increase}")
elif (current_price >= 30 and current_price < 80) and (average_monthly_sale >=500 and average_monthly_sale < 1200):
    increase = current_price * 0.15
    new_price = current_price + increase
    print(f"The new price of the product is: US$ {new_price} | increase: US$ {increase}")
elif (current_price >= 80) and (average_monthly_sale >= 1200):
    decrease = current_price * 0.20
    new_price = current_price - decrease
    print(f"The new price of the product is: US$ {new_price} | Decrease: US$ {decrease}")
            
    