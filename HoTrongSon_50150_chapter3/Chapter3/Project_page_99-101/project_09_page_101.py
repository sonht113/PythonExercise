"""
Author: Ho Trong Son
Date: 24/07/2021
Program: project_09_page_101.py

Problem:
    9.  Write a program that receives a series of numbers from the user and allows the user to press the enter key
        to indicate that he or she is finished providing inputs. After the user presses the enter key, the program
        should print the sum of the numbers and their average.

"""
# Code here:
num = int(input("Enter a string of numbers: "))
total = 0
count = 0

for i in str(num):
    total += int(i)
    count += 1

average = total / count
print("Total of string = ", total, "\nAverage of string = ", round(average, 2))

# Result:
# Enter a string of numbers: 4
# Total of string =  4
# Average of string =  4.0