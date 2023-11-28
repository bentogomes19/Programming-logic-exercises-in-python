#Create a program that receives the person weight, calculates and displays:
#   A) The new weight, if the person gains weight by 15% of the typed weight.
#   B) The new weight, if the person loses weight by 20% of the typed weight.
#variables = person_weight, new_weight

person_weight = float(input("Type your actual weight (Lbs): "))
new_weight1 = (person_weight * 0.15) + person_weight
print(f"Your new weight if you gains weight by 15% of the typed weight is: {new_weight1} Lbs")
new_weight2 =  person_weight  - (person_weight * 0.20) 
print(f"Your new weight if you loses weight by 20% of the typed weight is: {new_weight2} Lbs")