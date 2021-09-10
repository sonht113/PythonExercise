"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_02_page_92.py
Problem:
    2.  The factorial of an integer N is the product of the integers between 1 and N, inclusive.
        Write a while loop that computes the factorial of a given integer N.

Solution:
"""

N = 7
gt = 1
count = N

while (0 < count <= 7):
    gt *= count
    count -= 1

print("Factorial of", N, "=", gt)
# Result:
# => Factorial of 7 = 5040