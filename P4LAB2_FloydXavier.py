# Xavier Floyd
# 7/4/2026
# P4LAB2
# A program that displays a multiplication table for an integer input by user through a loop

# Create variable for while-loop to check
check = " "

# A while loops that repeats unti check equals 'no'
while check != "no":

    # Get integer for multiplication from user
    userNum = int(input("Enter an integer: "))
    print()

    # Checks if integer from user is zero or higher
    if userNum >= 0:
        # A for loop that uses range create a sequence of numbers to multiply the integer by
        for num in range(1, 13):
            total = num * userNum
            print(f"{userNum} * {num} = {total}")
    else:
        print("This program does not handle negative numbers.")

    # User input to end or rerun program
    check = input("\nWould you like to run the program again? ")
    print()

print("Exiting Program...")
