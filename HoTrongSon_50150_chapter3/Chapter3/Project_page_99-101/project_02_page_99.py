"""
Author: Ho Trong Son
Date: 24/07/2021
Program: project_02_page_99.py

Problem:
    2.  Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is a right triangle.
        Recall from the Pythagorean theorem that in a right triangle, the square of one side
        equals the sum of the squares of the other two sides.

Solution:
"""
# Code here:
print("Enter the lengths of three sides of a triangle: ")
a = int(input("Edge A: "))
b = int(input("Edge B: "))
c = int(input("Edge C: "))

if a + b > c and b + c > a and a + c > b:
    if pow(a, 2) == pow(b, 2) + pow(c, 2) or pow(b, 2) == pow(a, 2) + pow(c, 2) or pow(c, 2) == pow(b, 2) + pow(a, 2):
        print("Is a right triangle")
    else:
        print("Not a right triangle")
else:
    print("Not a triangle")

# Result here:

# Enter the lengths of three sides of a triangle:
# Edge A: 5
# Edge B: 6
# Edge C: 8
# Not a right triangle
