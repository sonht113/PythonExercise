"""
Author: Ho Trong Son
Date: 11/07/2021
Program: project_09_page_63.py
PROBLEM:
    9) Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
    • A kilometer represents 1/10,000 of the distance between the North Pole and
    the equator.
    • There are 90 degrees, containing 60 minutes of arc each, between the North
    Pole and the equator.
    • A nautical mile is 1 minute of an arc.

SOLUTION"
    ....
"""
# Code here:
Kilometers = int(input("Enter the amount of kilometers:"))
degreesPerMin = 90 * 60
onekilo = degreesPerMin / 10000
nauticalmile = onekilo * Kilometers
print(Kilometers, "is", nauticalmile, "Nautical miles")

# => Result:
# Enter the amount of kilometers:54
# 54 is 29.160000000000004 Nautical miles