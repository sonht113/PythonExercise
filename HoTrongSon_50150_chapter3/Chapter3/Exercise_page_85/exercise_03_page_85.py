"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_03_page_85.py
PROBLEM:
    3.  Write a loop that counts the number of space characters in a string. Recall that the
        space character is represented as ' '.

SOLUTION:
"""
# Code here:

name = "Ho Trong Son"
count = 0

for i in name:
    if i == ' ':
        count += 1

print("There are", count, "space characters in the string", name)

# Result:
# => There are 2 space characters in the string Ho Trong Son