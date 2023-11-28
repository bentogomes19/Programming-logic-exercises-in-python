#MAKE A PROGRAM THAT RECEIVES THE NUMBER OF HOURS WORKED, THE MINIMUM WAGE AMOUNT AND THE NUMBER OF HOURS
#EXTRAS WORKED, CALCULATE AND SHOW THE SALARY TO BE RECEIVED, FOLLOWING THE RULES BELOW:
# A) THE HOUR WORKED IS WORTH 1/8 OF THE MINIMUM WAGE;
# B) OVERTIME IS WORTH 1/4 OF THE MINIMUM WAGE;
# C) GROSS SALARY IS EQUIVALENT TO THE NUMBER OF HOURS WORKED MULTIPLIED BY THE VALUE OF THE HOUR WORKED;
# D) THE AMOUNT TO BE RECEIVED FOR OVERTIME IS EQUIVALENT TO THE NUMBER OF OVERTIME WORKED MULTIPLIED
#FOR THE OVERTIME PRICE;
# E) THE SALARY TO BE RECEIVED IS EQUIVALENT TO THE GROSS SALARY PLUS THE AMOUNT TO BE RECEIVED FOR OVERTIME;

# variables = hours_worked, min_wage, hours_extra, vl_hw, vl_hex, salary, amount_receive, sal_receive
hours_worked = int(input("Type the number of hours worked: "))
min_wage = float(input("Type the minimum wage amount US$: "))
hours_extra = int(input("Type the number of hours extra worked: "))

vl_hw = (min_wage * 1) / 8
vl_hex = (min_wage * 1) / 4
salary = hours_worked * vl_hw
amount_receive = hours_extra * vl_hex
sal_receive = salary + amount_receive
print(f"The amount to receive is: US$ {sal_receive}")