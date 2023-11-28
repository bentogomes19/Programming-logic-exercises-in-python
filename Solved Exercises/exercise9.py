#Make a program that receives two numbers, calculates and displays the division of the first number
#for the second. Knowing that the second number can't be zero, so, won't be necessary to worry with
#validations.
#variables = num1, num2, division

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))

if num2 == 0:
    print("THE SECOND NUMBER CANNOT BE ZERO!!")
else:
    division = num1 / num2
    print(f"The result a divison between two numbers is: {division}")