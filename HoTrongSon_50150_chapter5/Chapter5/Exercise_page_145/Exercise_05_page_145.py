"""
Author: Ho Trong Son
Date: 18/08/2021
Program: Exercise_05_page_145.py
Problem:
    5.  Assume that data refers to a list of numbers, and result refers to an empty list. Write a loop that adds
        the nonzero values in data to the result list, keeping them in their relative positions and excluding the
        zeros.
Solution:
    Display result:
        [25, 11, 19, 13, 8, 45]

"""

data = [25, 11, 19, 13, 8, 0, 45]
resultNewData = []

for value in data:
    if value != 0:
        resultNewData.append(value)

print(resultNewData)
