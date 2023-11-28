price = float(input("Type the value of the product (US$): "))
origin_code = int(input("Type the origin code between 1 to 30: "))
if origin_code == 1:
    print("South")
elif origin_code == 2:
    print("North")
elif origin_code == 3:
    print("Eeast")
elif origin_code == 4:
    print("West")
elif origin_code == 5 or origin_code == 6:
    print("Northeast")
elif origin_code >= 7 and origin_code <= 9:
    print("Southeast")
elif origin_code >= 10 and origin_code <= 20:
    print("West Center")
elif origin_code >= 21 and origin_code <= 30:
    print("Northeast")