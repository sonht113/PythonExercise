"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_02_page_118.py
Problem:
    2.  Using the value of data from Exercise 1, write the values of the following expressions:
        a.  data.endswith('i')
        b.  " totally ".join(data.split())

Solution:
    Display result:
        a) False
        b) Python totally rules!

"""

string = 'Python rules!'

print('a)', string.endswith('i'))
print('b)', " totally ".join(string.split()))
