#Make a program that receives the year of birth of the user and the actual year, calculates and displays
#A) The age in years: 
#B) The age in months:
#C) The age in days:
#D) The age in weeks:

birthday = int(input("Type you year of birth: "))
actual_year = int(input("Type the actual year: "))
years = actual_year - birthday
months = years * 12
days = months * 30
weeks = days / 7
print(f"The age in years: {years}")
print(f"The age in months: {months}")
print(f"The age in days: {days}")
print(f"The age in weeks: {weeks}")