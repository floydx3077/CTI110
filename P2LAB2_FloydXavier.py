# Xavier Floyd
# 6/20/2026
# P2LAB2
# A program that creates a dictonary of MPG information on car brands then calculates and display how much gallons of gas are needed for travel

# Dictonary of cars
automobileMPG = {
  "Camaro": 18.21,
  "Prius": 52.36,
  "Model S": 110,
  "Silverado": 26
}

# Get keys from dict and dispaly to user
print(automobileMPG.keys())

# Get a car from user
vehicle = input("\nEnter a vehicle to see it's mpg: ")

# Get mpg for the given car then display to user
mpg = automobileMPG.get(vehicle)

print(f"\nThe {vehicle} gets {mpg} mpg.")

# Get miles from user
miles = float(input(f"\nHow many miles will you drive the {vehicle}: "))

# Calculate gallons needed for distance
gallons = float(miles / mpg)

# Display the results
print(f"\n{gallons:.2f} gallon(s) of gas are needed to rive the Prius {miles:.2f} mpg.\n")