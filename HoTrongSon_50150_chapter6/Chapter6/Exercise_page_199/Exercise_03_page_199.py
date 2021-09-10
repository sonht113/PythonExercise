"""
Author: Ho Trong Son
Date: 01/09/2021
Program: Exercise_03_page_199.py
Problem:

    3.  Write the code for a reducing that creates a single string from a list of strings named words.

Solution:
    Result:
        You're a my girl friend

"""

from functools import reduce


def main():
    listWords = ["You're", "a", "my", "girl", "friend"]
    print(reduce(lambda x, y: x + " " + y, listWords))


if __name__ == '__main__':
    main()
