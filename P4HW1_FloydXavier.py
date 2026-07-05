# Xavier Floyd
# 7/4/2026
# P4HW1
# A program that calculates the min, max, sum, and average of the module grades entered by the user.

'''
Pseudocode:
Ask the user how many scores they want to enter: integer
Set a counter variable to 1
Create an empty list to store the scores

Use a while loop that continues while the counter is less than or equal to the amount of scores:
Ask the user to enter a score for the current count: float
Check if the score is between 0 and 100; if valid, add it to the list and increment the counter, otherwise keep prompting until a valid score is entered and then add it and increment the counter.

Find the lowest grade in the list using min()
Find the average of the list by dividing sum() by len()
Display the results section showing the lowest grade, modified list, and average score
Use conditional statements to assign a letter grade based on the average score then display (A for 90+, B for 80–89, C for 70–79, D for 60–69, otherwise F).
'''


# Get amount of scores user wants to find the average of 
amount = int(input("How many scores do you want to enter? "))
count = 1
moduleList = []

# Get grades of each module from the user using a while loop to append to a list
while count <= amount:
    item = float(input(f"Enter score #{count}: "))
    # Check if score is between or equal to 0 and 100 
    if item >= 0 and item <= 100:
        moduleList.append(item)
        count += 1        
    # If not, then user is put into another while loop that repeats until user enters a score that fulfill criteria
    else:
        check = " "
        while check != "good":
            print("\nINVALID Score Entered!!!\nScore should be between 0 and 100")
            item = float(input(f"\nEnter score #{count} again: "))
            if item >= 0 and item <= 100:
                moduleList.append(item)
                check = "good"
                count += 1



# Find the lowest grade in list
lowestGrade = min(moduleList)

# Find the average of list by dividing the sum by length
averageGrades = sum(moduleList) / len(moduleList)

# Display the results to the user
print("\n------------Results------------")

print(f'{"Lowest Grade":<15}: {lowestGrade:.1f}')
print(f'{"Modified List":<15}: {moduleList}')
print(f'{"Scores Average":<15}: {averageGrades:.2f}')
if averageGrades >= 90:
    print(f'{"Your grade is":<15}: A')
elif averageGrades < 90 and averageGrades >= 80:
    print(f'{"Your grade is":<15}: B')
elif averageGrades < 80 and averageGrades >= 70:
    print(f'{"Your grade is":<15}: C')
elif averageGrades < 70 and averageGrades >= 60:
    print(f'{"Your grade is":<15}: D')
else:
    print(f'{"Your grade is":<15}: F')
print("-------------------------------")