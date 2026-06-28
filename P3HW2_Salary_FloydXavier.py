# Xavier Floyd
# 6/27/2026
# P3LAB
# A program that calculates and displays the pay information of an employee from the payrate and hours worked

'''
Asks the user to enter name of employee: name
Ask user to enter number of hours the employee worked this week as a float: hours
Ask user to enter employee's pay rate as a float: payrate
Create if statement to check if employee has worked overtime which is more than 40 hours: if hours > 40
If yes for overtime, assign regular hours to max of 40, find overtime hours by subtracting 40 from hours variable then find overtime pay which should be 1.5 times their normal pay rate: regHour, overtimeHours, overtimePay
If no for overtime, assign regular hours equal to hours variable then assign overtime hours and pay equal to 0
Calculate amount employee should be paid for regular hours worked by multiplying regHour variable by payrate variable: reghourPay
Calculate gross pay be adding reghourPay and overtimePay: grossPay
Display all following pay information to the user: Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay
'''

# Get the employee information
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))

# Check if employee has worked overtime
if hours > 40:
    regHour = 40
    overtimeHours = hours - 40
    overtimePay = float(overtimeHours * payrate * 1.5)
else:
    regHour = hours
    overtimeHours = 0
    overtimePay = 0

# Calculate regular hours pay and gross pay
reghourPay = float(regHour * payrate)
grossPay = float(reghourPay + overtimePay)

# Display employee pay information
print("-------------------------------")
print(f"Employee name: {name}\n")
print("Hours Worked     Pay Rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f"{hours:<16.1f} {payrate:<12.1f} {overtimeHours:<12.1f} {overtimePay:<16.2f} ${reghourPay:<14.2f} ${grossPay:.2f}")