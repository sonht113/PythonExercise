"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_04_page_85.py
PROBLEM:
    4.  Assume that the variables x and y refer to strings. Write a code segment that prints
        these strings in alphabetical order. You should assume that they are not equal.

SOLUTION:
"""
# Code here:
x = "Ho Trong Son"
y = "Json"

words = [x, y]
words.sort(key=lambda k: k.lower())

for word in words:
    print(word)

# Result:
# Ho Trong Son
# Json