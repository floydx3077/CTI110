# Xavier Floyd
# 6/20/2026
# P2LAB1
# A program that calculates the diameter, circumference, and area of a circle using the radius

#Import math module to use math.pi
import math

# Get Radius from the user
radius = float(input("What is the radius of the circle? "))


# Calculate the diameter then display with 1 decimal point
diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}\n")


# Calculate the circumference then display with 2 decimal points
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {circumference:.2f}\n")


# Calculate the area then display with 3 decimal points
area = math.pi * radius**2
print(f"The area of the circle is {area:.3f}\n")

