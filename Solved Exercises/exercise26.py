user_numb1 = int(input('Type a number: '))
user_numb2 = int(input('Type a second number: '))
user_choice = int(input('Type a number between 1 and 4: 1|2|3|4|: '))

if user_choice ==1:
    media = (user_numb1 + user_numb2)/2 # media between the typed numbers
    print(f'the media between your numbers is: {media}')
elif user_choice ==2:
    if user_numb1 > user_numb2:
        sub = user_numb1 - user_numb2 # Subtraction between the typed numbers
        print(sub)
    elif user_numb2 > user_numb1:
        sub = user_numb2 - user_numb1 # Subtraction between the typed numbers
        print(sub)
elif user_choice ==3:
        mult = user_numb1 * user_numb2 # multiplication between the typed numbers
        print(mult)
elif user_choice ==4: 
        division = user_numb1 / user_numb2 # division between the first number by tthe second number
        print(division)
if user_choice  > 5:
    print("ERROR")

        
