#An employee receives a fixed salary plus a 4% commission over the sales. Create a program that receives
#the fixed salary of the employee and the value of your sales, calculates and displays the commission
#and your final salary.
#variables = fixed_salary, sales, commission, final_salary

fixed_salary = float(input("Type your fixed salary in the company (US$): "))
sales = float((input("Type the value of your sales (US$): ")))
commission = sales * 0.04
print(f"The commission is: U$ {commission}")
final_salary = fixed_salary + commission
print(f'Your final salary plus the commission will be: US$ {final_salary}')