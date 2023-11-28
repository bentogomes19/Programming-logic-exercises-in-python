#Make a program that receives the salary of an employee, calculates and displays the new salary 
#knowing that this has been increased by 25%

sal = float(input("Type your salary (US$): "))
new_sal = sal + (sal * 25/100)
print(f"Your new salary is: US$ {new_sal}")