"""
Author: Ho Trong Son
Date: 24/07/2021
Program: exercise_05_page_85.py
Problem:
    5.  Explain how to check for an invalid input number and prevent it being used in a program.
        You may assume that the user enters a number.

Set Case:
    A valid number is a number between 0 and 10 other than that it is invalid

Solution:
    Display result:
    =>   3 is Valid

    Explain:
        I use conditional statement to check if the given number satisfies the condition?
        If satisfy, it is valid, if not is invalid.

"""
# Code here:
num = 3
if 0 < num <= 10:
    print(num, "is Valid")
else:
    print(num, "is Invalid")