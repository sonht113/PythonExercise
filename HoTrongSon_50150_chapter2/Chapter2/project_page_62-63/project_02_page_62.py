"""
Author: Ho Trong Son
Date: 11/07/2021
Program: project_02_page_62.py
PROBLEM:
    2) You can calculate the surface area of a cube if you know the length of an edge.
    Write a program that takes the length of an edge (an integer) as input and prints
    the cube’s surface area as output.

SOLUTION:
    ....
"""

# You can calculate the surface area of a cube if you know the length of an edge. Write a program that takes the length of an edge (an integer) as input and prints the cube’s surface area as output.
# Code here:
surface = int(input("Enter the cube's edge: "))
result = 6 * (surface * surface)
print("The surface area is", result, "square units.")
# Enter the cube's edge: 3
# The surface area is 54 square units.
