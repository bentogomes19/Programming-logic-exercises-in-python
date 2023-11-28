#Knowing that the energy of a kilowatt costs a fifth of the minimum wage. 
#Create a program that receives the value of minimum wage and the kilowatt quantity used by a residence
#calculate and display: a) the value of each kilowatt b) the value that will be paid for that residence
#c) the amount to be paid with a 15% of discount
#variables = min_wage, quant_kw, value_kw, total_value, discount, value_discount

min_wage = float(input("Type the minimum wage (US$): "))
quant_kw = float(input("Type the kilowatt consumed in your residence:  "))
value_kw = min_wage /5
total_value = value_kw * quant_kw
discount = value_kw * 0.15
value_discount = total_value - discount
print(f"The value of each kilowatt is: US$ {value_kw}")
print(f"The value to be pay in your residence is: US$ {total_value}")
print(f"The value to be pay with a 15% of discount is: R$ {value_discount}")