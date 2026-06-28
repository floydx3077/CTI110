# Xavier Floyd
# 6/27/2026
# P3HW1
# Debugging a partial program with bugs and errors
'''
I'm not sure if I'm suppose to act as if this my own work that I'm correcting
or if I'm fixing/debugging another person's work, so I'll do the latter with
comments that indicate it.
'''
#------------------------------------------------------------------------------------
'''
FIX: Corrected Header by adding full name, date, assignment name, program description, and fixing the spacing
'''
# David Teter
# 6/27/2026
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

'''
FIX: Corrected the variable names, the text inside the input() function, and added float() function to convert input for the sake of the program
'''
# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

'''
FIX: Corrected the list by adding neccessary commas, adding the missing 6th variable, and fixing variable names
'''
# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

'''
FIX: Changed the high variable to use the proper function max() to find the highest grade in list, changed variable name of "sum" to "sumList" to avoid conflicts,
added expression "sumList / len(grades)" to variable avg to assign a value to it
'''
# TO DO: determine lowest, highest , sum and average for grades
low = float(min(grades))
high = float(max(grades))
sumList = float(sum(grades))
avg = float(sumList / len(grades))


'''
FIX: Added the missing display for the results
'''
print("\n------------Results------------")

print(f'{"Lowest Grade: ":<20}{low:.1f}')
print(f'{"Highest Grade: ":<20}{high:.1f}')
print(f'{"Sum of Grades: ":<20}{sumList:.1f}')
print(f'{"Average: ":<20}{avg:.2f}')
print("-------------------------------")

'''
FIX: Added elif checks to the ifelse statement, fixed the logical conditions to properly determine letter grade, and fixed formatting
'''
# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg < 90 and avg >= 80:
    print('Your grade is: B')
elif avg < 80 and avg >= 70:
    print('Your grade is: C')
elif avg < 70 and avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')