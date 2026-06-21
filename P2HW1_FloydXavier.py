# Xavier Floyd
# 6/21/2026
# P2HW1
# A program that calculates the travel expenses of user using basic math on the numbers entered; Redone for formatting

'''
Pseudocode:
Ask user for overall budget: Integer
Get user's destination: String
Ask for estimated gas expenses: Integer
Ask for estimated accommodation expenses: Integer
Ask for estimated food expenses: Integer
Add gas, hotel, and food to calculate total expenses
Subtract total expenses from the budget
Display the destination, total expenses, and remaining balance
'''

print("This program calculates and displays travel expenses\n")

# Get budget and destination from user
budget = float(input("Enter overall budget: "))
dest = input("\nEnter your travel destination: ")

# Get estimated costs of all expenses
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculations here
total_expense = float(gas + hotel + food)
balance = float(budget - total_expense)

# Display destination, total expenses, and balance
print("\n------------Travel Expenses------------")

print(f'{"Location: ":<20}{dest}')
print(f'{"Initial Budget: ":<20}${budget:.2f}')
print(f'{"Fuel: ":<20}${gas:.2f}')
print(f'{"Accomodation: ":<20}${hotel:.2f}')
print(f'{"Food: ":<20}${food:.2f}')
print("---------------------------------------")
print(f'{"\nRemaining Balance: ":<20}${balance:.2f}')
