# Xavier Floyd
# 7/4/2026
# P4HW2
# A program that calculates gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

'''
Psuedocode:
Create variables for employee name, employee count, overtime pay list, regular pay list, and gross pay list: name, count, overtimeList, regpayList, grossList
Use a while loop that repeats until the user enters "Done"
Ask the user to enter name of employee or "Done" to terminate: name
Create if statement to check if name is not equal to "Done"
Ask user to enter number of hours the employee worked this week as a float: hours
Ask user to enter employee's pay rate as a float: payrate
Add 1 to the employee count
Create if statement to check if employee has worked overtime which is more than 40 hours: if hours > 40
If yes for overtime, assign regular hours to max of 40, find overtime hours by subtracting 40 from hours variable, then find overtime pay which should be 1.5 times their normal pay rate: regHour, overtimeHours, overtimePay
If no for overtime, assign regular hours equal to hours variable then assign overtime hours and pay equal to 0
Calculate amount employee should be paid for regular hours worked by multiplying regHour variable by payrate variable: reghourPay
Calculate gross pay by adding reghourPay and overtimePay: grossPay
Add overtime pay, regular hour pay, and gross pay to their lists
Display all following pay information to the user: Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay
If name is equal to "Done", display total number of employees, total overtime pay, total regular pay, and total gross pay
'''

# Create variables for while-loop and totals
name = " "
count = 0
overtimeList = []
regpayList = []
grossList = []

# A while loop that repeats until the user enters "Done"
while name != "Done":
    name = input("Enter employee's name or \"Done\" to terminate: ")

    # Continue collecting employee pay information if the user did not enter "Done"
    if name != "Done":
        hours = float(input("Enter number of hours worked: "))
        payrate = float(input("Enter employee's pay rate: "))

        # Add one to the employee count
        count += 1

        # Check if employee has worked overtime
        if hours > 40:
            regHour = 40
            overtimeHours = hours - 40
            overtimePay = float(overtimeHours * payrate * 1.5)
        else:
            regHour = hours
            overtimeHours = 0
            overtimePay = 0
        
        # Calculate regular pay and gross pay
        reghourPay = float(regHour * payrate)
        grossPay = float(reghourPay + overtimePay)

        # Add each pay amount to its list for final totals
        overtimeList.append(overtimePay)
        regpayList.append(reghourPay)
        grossList.append(grossPay)

        # Display employee pay information
        print("-------------------------------")
        print(f"Employee name: {name}\n")
        print("Hours Worked     Pay Rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay")
        print("-------------------------------------------------------------------------------------")
        print(f"{hours:<16.1f} {payrate:<12.1f} {overtimeHours:<12.1f} {overtimePay:<16.2f} ${reghourPay:<14.2f} ${grossPay:.2f}\n")
    else:
        # Display final totals after the user enters "Done"
        print("\nTotal number of employees entered: ", count)
        print(f"Total amount paid for overtime: ${sum(overtimeList):.2f}")
        print(f"Total amount paid for regular hours: ${sum(regpayList):.2f}")
        print(f"Total amount paid in gross: ${sum(grossList):.2f}")
