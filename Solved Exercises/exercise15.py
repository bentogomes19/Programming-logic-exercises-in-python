#Make a program that calculates and displays the area of the trapezoid
# You need to know: A = ((larger base + shorter base)* height)/2
larger_base = float(input("Type the larger base of the trapezoid: "))
shorter_base = float(input("Type the shorter base of the trapezoid: "))
height = float(input("Type the height of the trapezoid: "))
area = ((larger_base + shorter_base) * height)/2
print(f"The area of the trapezoid is: {area} m2")