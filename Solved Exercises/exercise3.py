#Make a program that receive the salary of employee and percentage increase, calculate and show
#the value of increase and the new salary

#variables = sal, increase, new_salary, value_increase
sal = float(input("Type your salary (US$): "))
increase = int(input("Type the percentage increase %: "))
value_increase = sal * increase/100
print(f"The value increase was: US${value_increase}")
new_salary = value_increase + sal
print(f"Your new salary will be: US$ {new_salary}")
