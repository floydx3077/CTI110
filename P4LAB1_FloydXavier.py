# Xavier Floyd
# 7/4/2026
# P4LAB1
# A program that draws a triangle and a square using loops

import turtle

# Create the drawing scene and turtle, and assign unique colors
window = turtle.Screen()
window.bgcolor("lightgreen")
t = turtle.Turtle()
t.color("red")


# Draw the square part of the house using a while loop
square = 0
while square < 4:
    t.forward(150)
    t.left(90)
    square += 1

# Repositioning to return the turtle to the top of the square so the roof is properly placed
t.left(90)
t.forward(150)
t.right(90)

# A little color customization for roof
t.color("darkred")

# Draw the triangle roof using a for loop
for i in range(3):
    t.forward(150)
    t.left(120)


window.mainloop()