"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_04_page_125.py
Problem:
    4.  Write a code segment that prints the names of all of the items in the current working directory.
Solution:
    Display result:
        Exercise_03_page_125.py
        Exercise_01_page_125.py
        Exercise_02_page_125.py
        Exercise_04_page_125.py
        Exercise_05_page_125.py

"""
import os

for file in os.listdir():
    print(file)

