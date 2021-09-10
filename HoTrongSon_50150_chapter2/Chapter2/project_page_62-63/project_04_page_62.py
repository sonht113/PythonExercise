"""
Author: Ho Trong Son
Date: 11/07/2021
Program: project_04_page_62.py
PROBLEM:
    4) Write a program that takes the radius of a sphere (a floating-point number) as
    input and then outputs the sphere’s diameter, circumference, surface area, and
    volume.

SOLUTION:
    ....
"""
#Code here:
import math

radius = float(input("Radius = "))
diameter = radius * 2
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4 / 3 * math.pi * radius * radius * radius
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area : ", surfaceArea)
print("Volume ", volume)

# => Result:
# Radius = 3
# Diameter:  6.0
# Circumference:  18.84955592153876
# Surface area :  113.09733552923255
# Volume  113.09733552923255
