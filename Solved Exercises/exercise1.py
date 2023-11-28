print("WELCOME TO WISCONSIN HIGH SCHOOL!")
print("------------------------------")

g1 = float(input('grade1: '))
g2 = float(input('grade2: '))
g3= float(input('grade3: '))
ag = (g1 + g2 + g3)/3
#grade of the student
if (ag >= 5):
    print("Congratulations! You're approved for the next year!")
    print(ag)
else:
    print("You're repproved")

if (ag <= 9):
    print("That's nice! it's a good grade")   