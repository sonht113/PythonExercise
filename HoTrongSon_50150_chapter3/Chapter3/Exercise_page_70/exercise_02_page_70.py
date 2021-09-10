"""
Author: Ho Trong Son
Date: 23/07/2021
Program: exercise_02_page_70.py

PROBLEM:
    2.  Write a loop that prints your name 100 times. Each output should begin on a new line.

SOLUTION:
"""
# Code here:
name = "Ho Trong Son"

for i in range(100):
    print(name, "(" + str(i+1) + ")")

# Result:
#     Ho Trong Son (1)
#     ...
#     ...
#     ...
#     Ho Trong Son (100)