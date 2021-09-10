"""
Author: Ho Trong Son
Date: 05/09/2021
Program: Project_03_page203.py
Problem:
    3.  Elena complains that the recursive newton function in Project 2 includes an extra argument for the estimate.
        The function’s users should not have to provide this value, which is always the same, when they call this
        function. Modify the definition of the function so that it uses a keyword argument with the appropriate
        default value, and call the function without a second argument to demonstrate that it solves this problem.

Solution:
    Display result
        Enter a positive number or 'E' to exit: 123
        The program's estimate:  11.090536508377188
        Python's estimate:  11.090536506409418
        Enter a positive number or 'E' to exit: e

"""
# Code here:
import math


def newton(x, estimate = 1.0):
    tolerance = 0.000001
    if abs(x - pow(estimate, 2)) <= tolerance:
        return estimate
    else:
        estimate = newton(x, (estimate + x / estimate) / 2)
    return estimate


def main():
    while True:
        x = input("Enter a positive number or 'E' to exit: ")
        if x.upper() == 'E':
            break
        print("The program's estimate: ", newton(float(x)))
        print("Python's estimate: ", math.sqrt(float(x)))


if __name__ == "__main__":
    main()
