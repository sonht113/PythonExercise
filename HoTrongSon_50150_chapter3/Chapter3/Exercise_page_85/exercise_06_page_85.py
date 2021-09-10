"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_06_page_85.py
Problem:
    6.  Construct truth tables for the following Boolean expressions:
        a.  not (A or B)
        b.  not A and not B

Solution:
"""
# Code here:
a = 0
b = 1

print("%4s %4s %10s %12s" % ("A", "B", "!A or !B", "!A and !B"))
print("%4s %4s %10s %12s" % (a, b, not (a or b), not a and not b))

# Result:
   # A    B   !A or !B    !A and !B
   # 0    1      False        False