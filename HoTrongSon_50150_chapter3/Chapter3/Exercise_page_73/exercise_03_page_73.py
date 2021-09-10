"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_03_page_73.py
PROBLEM:
    3.  Write a format operation that builds a string for the float variable amount that has
        exactly two digits of precision and a field width of zero.

SOLUTION:
"""
# Code here:

import math
amount = math.pi
print(f"{amount:0.2f}")


# Result:
#       3.14