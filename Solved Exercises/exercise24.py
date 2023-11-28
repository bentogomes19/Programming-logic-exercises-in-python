#Make a program that receive the user password, if the answer of the user not compatible with password
#displays "Invalid Password", if not, them print "allowed acess"

password = 4531
user_password = int(input("Type your password here: "))

while user_password != password:
    print('Invalid password')
    user_password = int(input("Type your password here: "))
else:
    print('Allowed Acess')