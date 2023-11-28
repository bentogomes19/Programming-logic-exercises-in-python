#Make a program that receives an employee's basic salary, calculates and displays the salary to be received
#knowing that the employee has a 5% bonus on the base salary and pays 7% of tax on this salary
#variables = basic_salary, receive_salary, bonus, tax, 

basic_salary = float(input("Type your basic salary (US$): "))
bonus = basic_salary * 5/100
tax = basic_salary * 7/100
receive_salary =  basic_salary + bonus - tax
print(f"Your salary to receive will be: US$ {receive_salary}")
print(f"You'll receive a bonus: US$ {bonus}")
print(f"Here the value of tax you will pay: US$ {tax}")