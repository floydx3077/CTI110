# Xavier Floyd
# 6/13/2026
# P1HW2
# A program that calculates the travel expenses of user using basic math on the numbers entered

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
budget = int(input("Enter overall budget: "))
dest = input("Enter your travel destination: ")

# Get estimated costs of all expenses
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

# Calculations here
total_expense = gas + hotel + food
balance = budget - total_expense

# Display destination, total expenses, and balance
print("\n----------Travel Expenses----------")

print("Location: ", dest)
print("Initial Budget: ", budget)
print("\n")
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print("\n")
print("Remaining Balance: ", balance)
