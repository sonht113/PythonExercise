"""
Author: Ho Trong Son
Date: 18/08/2021
Program: Exercise_06_page_145.py
Problem:

    6.  Write a loop that replaces each number in a list named data with its absolute value.
Solution:
    Display result:
        [23, 11, 20, 43, 0, 26, 10]

"""

data = [-23, -11, 20, -43, 0, 26, -10]

for item in range(0, len(data)):
    data[item] = abs(data[item])

print(data)
