"""
Author: Ho Trong Son
Date: 11/07/2021
Program: project_06_page_62.py
PROBLEM:
    6) The kinetic energy of a moving object is given by the formula KE 5 (1 2 / )mv2
    where m is the object’s mass and v is its velocity. Modify the program you created
    in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

SOLUTION:
    ....
"""
# Code here:
mass = float(input("Mass: "))
velocity = float(input("Velocity: "))
KE = 0.5 * mass * velocity ** 2
momentum = mass * velocity
print("The object's momentum is " + str(momentum))
print("The object's kinetic energy is " + str(KE))

# => Result:
# Mass: 3
# Velocity: 3
# The object's momentum is 9.0
# The object's kinetic energy is 13.5
