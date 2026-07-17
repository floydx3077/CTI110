# Xavier Floyd
# 7/12/2026
# LLM_LAB1
# A program that practices working with an AI language model to generate a Python script based on specific functional requirements

import random

print("Welcome to the Number Guessing Game!")

# A while loop to keep asking until the user enters a valid menu choice
while True:
    print("\nMenu")
    print("1. Start Game")
    print("2. Exit")

    choice = input("Enter your choice: ")

    # Check if the choice is valid
    if choice == '1' or choice == '2': 
        break
    else: 
        print("Invalid choice. Please enter 1 or 2.")

# Start the game if the user selected option 1 or exit if the user selected option 2
if choice == "1":
   
   # While loop for the number guessing game, continues if user keeps entering 'yes'
    while choice == "1":
        # Generate a random number between 1 and 100, then sets variable for chances and variable whether number was guessed correctly
        number = random.randint(1, 100)
        chances = 5
        guessed_correctly = False

        print("\nI picked a number between 1 and 100.")
        print("You have 5 chances to guess it.")

        # While loop that continues until the user runs out of chances
        while chances > 0:
            guess = int(input("\nEnter your guess: "))
            chances -= 1

            # Check if the guess is correct
            if guess == number:
                print("Correct! You guessed the number!")
                guessed_correctly = True
                break

            # Find the difference between the guess and the number
            difference = abs(number - guess)

            # Give a hint based on how close the guess is
            if difference <= 3:
                print("Blazing hot!")
            elif difference <= 5:
                print("Super hot!")
            elif difference <= 10:
                print("Hot!")
            elif difference <= 15:
                print("Warm!")
            elif difference <= 20:
                print("Lukewarm!")
            else:
                print("Cold!")

            if chances > 0:
                print(f"You have {chances} chances remaining.")

        # Display the correct number if the user did not guess it
        if not guessed_correctly:
            print(f"\nYou ran out of chances. The number was {number}.")

        # Ask the user if they want to play again, exits if the user does not enter yes
        continue_game = input("\nWould you like to play again? (yes/no): ").lower()
        if continue_game != "yes":
            print("Thanks for playing!")
            break
else:
    print("Exiting Program...")