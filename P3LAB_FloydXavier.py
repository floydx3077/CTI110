# Xavier Floyd
# 6/27/2026
# P3LAB
# A program that find the number of dollars, quarters, dimes, nickels, and pennies needed to make the amount of money entered by the user

# Get the amount of money from user
money = float(input("Enter the amount of money as a float: $"))

# Check if money is greater than zero, if so then proceed, if not it goes to else and display 'No change.'
if money > 0:
    money = (money * 100)

    # Find how many dollars are in the amount, then display to user if there's more than 0
    dollars = int(money // 100)
    money = money - (dollars * 100)
    if dollars > 0:
        if dollars == 1: print(f"{dollars} Dollar")
        else: print(f"{dollars} Dollars")
        
    # Find how many quarters are in the amount, then display to user if there's more than 0
    quarters = int(money // 25)
    money = money - (quarters * 25)
    if quarters > 0:
        if quarters == 1: print(f"{quarters} Quarter")
        else: print(f"{quarters} Quarters")

    # Find how many dimes are in the amount, then display to user if there's more than 0
    dimes = int(money // 10)
    money = money - (dimes * 10)
    if dimes > 0:
        if dimes == 1: print(f"{dimes} Dime")
        else: print(f"{dimes} Dimes")
        
    # Find how many nickels are in the amount, then display to user if there's more than 0
    nickels = int(money // 5)
    money = money - (nickels * 5)
    if nickels > 0:
        if nickels == 1: print(f"{nickels} Nickel")
        else: print(f"{nickels} Nickels")
        
    # Find how many pennies are in the amount, then display to user if there's more than 0
    pennies = int(money // 1)
    money = money - (pennies * 1)
    if pennies > 0:
        if pennies == 1: print(f"{pennies} Penny")
        else: print(f"{pennies} Pennies")        
 
else:
    print("No change.")