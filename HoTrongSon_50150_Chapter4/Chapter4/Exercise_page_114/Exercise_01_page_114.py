"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_01_page_114.py
Problem:
    1.  Translate each of the following numbers to decimal numbers:
        a.  11001(2)
        b.  100000(2)
        c.  11111(2)

Solution:
    Result:
        a) The decimal number of bit string '11001' is: 25
        b) The decimal number of bit string '100000' is: 32
        c) The decimal number of bit string '11111' is: 31


"""
arrayBit = ['11001', '100000', '11111']

for element in arrayBit:
    decimalNumber = 0
    exponent = len(element) - 1
    for digit in element:
        decimalNumber = decimalNumber + int(digit) * 2 ** exponent
        exponent = exponent - 1
    print("The decimal number of bit string '" + element + "' is:", decimalNumber)

