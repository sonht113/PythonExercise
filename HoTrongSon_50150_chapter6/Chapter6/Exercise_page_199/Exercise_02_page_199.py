"""
Author: Ho Trong Son
Date: 01/09/2021
Program: Exercise_02_page_199.py
Problem:

    2.  Write the code for a filtering that generates a list of the positive numbers in a list named numbers.
        You should use a lambda to create the auxiliary function.

Solution:
    Result:
        [1, 3]

"""

def main():
    listNumbers = [1, -5, 3, -6, -25]
    print(list(filter(lambda x: x > 0, listNumbers)))


if __name__ == '__main__':
    main()
