#Jon recieved your salary and needs to pay two overdue bills. Because of the delay, he will need to pay
# 2% penalty about each bills. Make a program thats calculates and displays how much will be left of
# Jon's salary?

jon_salary = 750
bill1 = 7500
bill2 = 800
penalty = bill1 * 0.02
penalty2 = bill2 * 0.02
left_of_jonsal = jon_salary - (bill1 + penalty) - (bill2 + penalty2)
print(f"The left of Jons salary it's : US$ {left_of_jonsal}")