"""
Author: Ho Trong Son
Date: 01/09/2021
Program: Exercise_01_page_199.py
Problem:
    1.  Write the code for a mapping that generates a list of the absolute values of the numbers in a list
        named numbers.
Solution:
    Result:
        [[1, 5, 3, 6, 25]

"""

def main():
    listNumbers = [1, -5, 3, -6, -25]
    print(list(map(abs, listNumbers)))


if __name__ == '__main__':
    main()
