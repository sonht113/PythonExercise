"""
Author: Ho Trong Son
Date: 23/07/2021
Program: exercise_01_page_70.py
PROBLEM:
    1.  Write the outputs of the following loops:
        a.  for count in range(5):
                print(count + 1, end = " ")
        b.  for count in range(1, 4):
                print(count, end = " ")
        c.  for count in range(1, 6, 2):
                print(count, end = " ")
        d.  for count in range(6, 1, –1):
            print(count, end = " ")

SOLUTION:
"""
# Code here:
# 1
for count in range(5):
    print(count + 1, end=" ")
# 2
print()
for count in range(1, 8):
    print(count, end=" ")
# 3
print()
for count in range(1, 6, 2):
    print(count, end=" ")
# 4
print()
for count in range(5, 1, -2):
    print(count, end=" ")

# Result:
# a) 1 2 3 4 5
# b) 1 2 3 4 5 6 7
# c) 1 3 5
# d) 5 3