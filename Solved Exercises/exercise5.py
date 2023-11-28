#You need to create a program that receives the value of deposit and the interest tax, calculates and
#displays the value of income and the total value after the income
#variables = deposit, interest_tax, income, total_value
deposit = float(input("Type the value of deposit: (US$): "))
interest_tax = float(input("Type the interest tax (%): "))
income = deposit * interest_tax/100
total_value = deposit + income
print(f"The total value after the income will be: US$ {total_value}")
