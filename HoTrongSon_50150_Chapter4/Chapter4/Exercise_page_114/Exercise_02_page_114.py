"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_02_page_114.py
Problem:
    2.  Translate each of the following numbers to binary numbers:
        a.  47(10)
        b.  127(10)
        c.  64(10)

Solution:
    Result:
        a.  101111
        b.  1111111
        c.  1000000

"""

def bit(decimal):
    if decimal == 0:
        print(0)
    else:
        bitString = ''
        while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            bitString = str(remainder) + bitString

    print(bitString)


element = [47, 127, 64]
for decimalNumber in element:
    bit(decimalNumber)
