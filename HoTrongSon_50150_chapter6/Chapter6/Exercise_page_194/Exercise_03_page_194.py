"""
Author: Ho Trong Son
Date: 01/09/2021
Program: Exercise_03_page_194.py
Problem:

    3.  What is the lifetime of a variable? Give an example.
Solution:
    Result:
        The lifetime of a variable is the time during which the variable stays in memory and is therefore accessible during program execution.

"""

def example(n):
    if n > 0:
        print(n)
        example(n - 1)


def main():
    example(5)


if __name__ == '__main__':
    main()
