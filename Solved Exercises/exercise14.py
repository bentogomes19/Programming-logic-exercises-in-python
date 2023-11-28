#Make a program that receives the weight in kilograms, calculates and displays this weight in grams

weight_kg = float(input("Type the weight in kilograms: "))
weight_grams = weight_kg * 1000
print(f'The conversion to grams it is: {weight_grams}')