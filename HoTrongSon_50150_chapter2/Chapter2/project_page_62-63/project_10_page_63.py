"""
Author: Ho Trong Son
Date: 11/07/2021
Program: project_10_page_63.py
PROBLEM:
    10) An employee’s total weekly pay equals the hourly wage multiplied by the total
    number of regular hours plus any overtime pay. Overtime pay equals the total
    overtime hours multiplied by 1.5 times the hourly wage. Write a program that
    takes as inputs the hourly wage, total regular hours, and total overtime hours and
    displays an employee’s total weekly pay.

SOLUTION:
    ....
"""
# Code here:
hourWage = float(input("What is your hourly wage?: "))
regularHours = float(input("How many regular hours did you work this week?: "))
overtimeHours = float(input("How many overtime hours did you have this week?: "))
overtimeWage = (1.5 * hourWage)
totalWeeklyPay = (hourWage * regularHours) + (overtimeHours * overtimeWage)
print("Your total weekly pay is: ", totalWeeklyPay)

# Result:
# What is your hourly wage?: 10000
# How many regular hours did you work this week?: 23
# How many overtime hours did you have this week?: 12
# Your total weekly pay is:  410000.0