"""
Author: Ho Trong Son
Date: 11/07/2021
Program: project_08_page_63.py
PROBLEM:
    8) Light travels at 3 *108 meters per second. A light-year is the distance a light beam
    travels in one year. Write a program that calculates and displays the value of a
    light-year.

SOLUTION:
    ....
"""

import math

secondsInOneYear = 365 * 24 * 60 * 60;
rate = 3 * math.pow(10, 8);
result = secondsInOneYear * rate;
print("The value of a light year is:", result)

# => result:
# The value of a light year is: 9460800000000000.0