#Caelon Gooden
#P2LAB
#10/2/2023
#Using math expressions
import math

#Get radius from user
radius = float(input('Enter the radius of a circle: '))
#Calculate circumference , diameter, and area
diameter = 2 * radius
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
#Display results
print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.3f}")
