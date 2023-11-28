#Make a program that receives two grades, calculates and displays the weighted average of these grades
#you need to consider that weight 2 is for the first grade and weight 3 is for the second grade
#variables = grade1, grade2, weighted_average
grade1 = float(input("Type your first grade: "))
grade2 = float(input("Type your second grade: "))
weighted_average = (grade1 * 2 + grade2 * 3) /5
print(f"Your weighted average is: {weighted_average}")