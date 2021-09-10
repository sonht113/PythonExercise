"""
Author: Ho Trong Son
Date: 24/07/2021
Program: project_01_page_99.py
Problem:
    1.  Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is an equilateral triangle.

Solution:
"""
# Code here:
print("Enter the lengths of three sides of a triangle: ")
a = int(input("Edge A: "))
b = int(input("Edge B: "))
c = int(input("Edge C: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Is an equilateral triangle")
    else:
        print("Not an equilateral triangle")
else:
    print("Not a triangle")

# Result here:
# Enter the lengths of three sides of a triangle:
# Edge A: 3
# Edge B: 2
# Edge C: 4
# Not an equilateral triangle