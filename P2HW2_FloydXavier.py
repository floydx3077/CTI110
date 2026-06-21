# Xavier Floyd
# 6/21/2026
# P2HW2
# A program that calculates the min, max, sum, and average of the module grades entered by the user.

'''
Pseudocode:
Ask user to input grades for each module: float (for each one)
Put each module variable into a list
Find the minimum of the list: using function min()
Find the maximum of the list: using function max()
Find the total sum of the list: using function sum()
Find the average of the list: using function len() to list's length, then dividing the sum by the length
Display the Lowest Grade (minimum), Highest Grade (maximum), Sum of Grades (sum), and Average (sum/len) to the user
'''

# Get grades of each module from the user
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Put each grade into a list
moduleList = [module1, module2, module3, module4, module5, module6]

# Find the lowest grade in list
lowestGrade = min(moduleList)

# Find the highest grade in list
highestGrade = max(moduleList)

# Find the total of list
sumGrades = sum(moduleList)

# Find the average of list by dividing the total by length
averageGrades = sumGrades / len(moduleList)

# Display the results to the user
print("\n------------Results------------")

print(f'{"Lowest Grade: ":<20}{lowestGrade:.1f}')
print(f'{"Highest Grade: ":<20}{highestGrade:.1f}')
print(f'{"Sum of Grades: ":<20}{sumGrades:.1f}')
print(f'{"Average: ":<20}{averageGrades:.2f}')
print("-------------------------------")