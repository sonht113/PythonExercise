"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_04_page_73.py
PROBLEM:
    4.  Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted
        in a column that is right-justified, with a field width of 12 and a precision of 2.

SOLUTION:
"""
# Code here:
salaries = [200.5665, 100.457, 300.123, 730.311]

for i in salaries:
    print(f"{i:12.2f}")

    # Result:
    #     200.57
    #     100.46
    #     300.12
    #     730.31