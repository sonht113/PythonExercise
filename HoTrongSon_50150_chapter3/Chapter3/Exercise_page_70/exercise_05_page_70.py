"""
Author: Ho Trong Son
Date: 23/07/2021
Program: exercise_05_page_70.py
PROBLEM:
    5.  Assume that the variable test string refers to a string. Write a loop that prints
        each character in this string, followed by its ASCII value.

SOLUTION:

    => J = 74; a = 97; s = 115; o = 111; n = 110;
"""
# Code here:
name = "Jason"
for i in name:
    print(i, "=", ord(i), end="; ")