"""
Author: Ho Trong Son
Date: 01/09/2021
Program: Exercise_04_page_182.py
Problem:

    4.  Explain what happens when the following recursive function is called with the value 4 as an argument:
            def example(n):
               if n > 0:
                    print(n)
                    example(n - 1)

Solution:
    Result:
        -   Print to the screen the numbers from 10 to 1
"""
def example(n):
    if n > 0:
        print(n)
        example(n - 1)


def main():
    example(10)

main()