"""
Author: Ho Trong Son
Date: 24/07/2021
Program: project_06_page_100.py

Problem:
    6.  The German mathematician Gottfried Leibniz developed the following method to approximate the value of π:
                                        π/4 = 1 - 1/3 + 1/5 - 1/7 + . . .
        Write a program that allows the user to specify the number of iterations used in this approximation and
        that displays the resulting value.

Solution:
"""
# code here:
import math

n = int(input("Enter the number of iterations: "))
result = 0
a = []

for i in range(1, (n*2), 2):
    a.append(i)

for i in range(0, len(a)-1, 2):
    a[i+1] = - a[i+1]

for i in a:
    result += 1/i

print("π/4 = ", math.pi/4)
print("The result after", n, "iterations is", result)


# Result here:
# Enter the number of iterations: 7
# π/4 =  0.7853981633974483
# The result after 7 iterations is 0.8209346209346211