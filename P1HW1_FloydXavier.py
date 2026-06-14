# Xavier Floyd
# 6/13/2026
# P1HW1
# A program that takes user input of numerical values and uses them in mathematical expressions

# Caculate Exponents
print("------------------Exponents-----------------\n")

# User input
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print("\n")

print(base, "raised to the power of", exponent, "is", base**exponent, "!!")
print("\n")

# Caculate Addition and Subtraction
print("----------Addition and Subtraction----------\n")

# User input
start_num = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))
print("\n")

print(start_num, "+", add, "-", subtract, "is equal to", start_num + add - subtract)
