#MAKE A PROGRAM THAT CALCULATES AND DISPLAYS THE MULTIPLICATION TABLE OF A NUMBER ENTERED BY THE USER

user_num = int(input("Type a random number: "))
print(f"0 * {user_num} = {0*user_num} ")
print(f"1 * {user_num} = {1*user_num} ")
print(f"2 * {user_num} = {2*user_num} ")
print(f"3 * {user_num} = {3*user_num} ")
print(f"4 * {user_num} = {4*user_num} ")
print(f"5 * {user_num} = {5*user_num} ")
print(f"6 * {user_num} = {6*user_num} ")
print(f"7 * {user_num} = {7*user_num} ")
print(f"8 * {user_num} = {8*user_num} ")
print(f"9 * {user_num} = {9*user_num} ")
print(f"10 * {user_num} = {10*user_num} ")

user_num2 = int(input('Type a random number: '))
count =0 
for count in range(10):
    print("%d x %d = %d" % (user_num2, count+1, user_num2*(count+1)))
