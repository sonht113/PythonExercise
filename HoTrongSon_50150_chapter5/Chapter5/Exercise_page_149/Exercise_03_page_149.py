"""
Author: Ho Trong Son
Date: 18/08/2021
Program: Exercise_03_page_149.py
Problem:
    3.  Use the function even to simplify the definition of the function odd presented in this section.
Solution:
    Display result:
        True

"""

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def odd(even):
    if even == False:
        return True
    else:
        return False

# main
print(odd(even(13)))

