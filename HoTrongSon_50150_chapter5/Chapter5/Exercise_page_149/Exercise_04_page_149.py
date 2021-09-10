"""
Author: Ho Trong Son
Date: 18/08/2021
Program: Exercise_04_page_149.py
Problem:
    4.  Define a function named summation. This function expects two numbers, named low and high, as arguments.
        The function computes and returns the sum of the numbers between low and high, inclusive.
Solution:
    Display result:
        5

"""

def summation(low, high):
    result = 0
    for index in range(low, high):
        result += index
    return result

low = 2
high = 4
print(summation(low, high))

