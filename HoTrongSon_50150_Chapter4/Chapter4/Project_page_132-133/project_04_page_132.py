"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_04_page_132.py
Problem:
    4.  Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and
        decimalToOctal.py, which convert numbers between the octal and decimal representations of integers.
        These scripts use algorithms that are similar to those of the binaryToDecimal and decimalToBinary
        scripts developed in Section 4-3.

Solution:
    Display result
        Enter a decimal integer: 14
        The octal representation is: 16
        The binary representation of 16 is: 14
"""

def swapEight(eightNumber):
    number = eightNumber
    length = len(eightNumber)
    eightNumber = int(eightNumber)
    total = 0
    for i in range(0, length):
        index = eightNumber % 10
        total += (index * pow(8, i))
        eightNumber //= 10

    print("The binary representation of", str(number), "is: ", total)


def decimalToOctal(decimal):
    if decimal == 0:
        print(0)
    else:
        string = ''
        while decimal > 0:
            remainder = decimal % 8
            decimal = decimal // 8
            string = str(remainder) + string
        return string

decimal = int(input("Enter a decimal integer: "))
print("The octal representation is: ", decimalToOctal(decimal))
swapEight(decimalToOctal(decimal))
