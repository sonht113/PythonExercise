"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_03_page_106.py
Problem:
    3.  Assume that the variable data refers to the string "myprogram.exe". Write the expressions that perform
        the following tasks:

Solution:
    Display result:
        n o s a J

"""

string = "Jason"
length = len(string)
for index in range(length - 1, -1, -1):
    print(string[index], end=' ')
