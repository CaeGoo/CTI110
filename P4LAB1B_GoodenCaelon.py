# Caelon Gooden
# 04/09/2025
# P4LAB1
# Use turtle and loops to draw a your initials 

#Import the turtle library 
import turtle

#Create a turtle object and window 
window = turtle.Screen()
t = turtle.Turtle()

#Set the turtle options
t.pensize(3)
t.pencolor("blue")
t.shape("arrow")

#Draw the letter C
#Turn pin to the left 
t.left(120)

t.penup()
for side in range(2):
    t.forward(10)
    t.left(12)
t.pendown()

#Begin marking for letter C

for side in range(23):
    t.forward(10)
    t.left(12)

#Relocate pin to draw letter G
    
t.penup()
t.left(30)
t.forward(50)
t.right(90)
t.forward(120)
t.left(120)
for side in range(2):
    t.forward(10)
    t.left(12)
t.pendown()

#Begin marking for letter G

for side in range(26):
    t.forward(10)
    t.left(12)

t.left(90)
t.forward(50)


#Wait for the user to close the window
window.mainloop()