#Caelon Gooden
# 04/09/2025
# P4LAB1
# Use turtle and loops to draw a square and a triangle

#Import the turtle library
import turtle

#Create a turtle object and window
window = turtle.Screen()
t = turtle.Turtle()

#Set the turtle options
t.pensize(3)
t.pencolor("blue")
t.shape("arrow")

#Code to draw shapes
for side in range(4):
    t.left(90)
    t.forward(100)

#While loop tha executes 3 times 
sides = 3
while sides > 0:
    t.left(120)
    t.forward(100)
    sides -= 1


#Wait for the user to close the window
window.mainloop()
