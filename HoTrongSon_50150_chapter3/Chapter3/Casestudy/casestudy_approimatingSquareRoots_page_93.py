"""
Author: Ho Trong Son
Date: 23/07/2021
Program: casestudy_approximatingSquareRoots_page_93.py
PROBLEM:
    Compute the square root of a number.
        1.  The input is a number.
        2.  The outputs are the program's estimate of the square root using Newton's method of
            successive approximations, and Python's own estimate using math.sqrt.

SOLUTION:
    => Display result:
            Enter a positive number: 3
            The program's estimate: 1.7320508100147274
            Python's estimate:  1.7320508075688772

"""

# Receive the input number from the user
import math
a = float(input("Enter number: "))
# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0
# Perform the successive approximations
while True:
    estimate = (estimate + a / estimate) / 2
    difference = abs(a - estimate ** 2)
    if difference <= tolerance:
        break
# Output:
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(a))