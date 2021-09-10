"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_05_page_114.py
Problem:
    5.  Translate each of the following numbers to decimal numbers:
        a.  47(16)
        b.  127(16)
        c.  AA(16)

Solution:
    Result:
        a.  71
        b.  295
        c.  170

"""
#Code here:
def sixteenToDecimal(sixteenNumber):
    LETTER = '0123456789ABCDEF'
    num = sixteenNumber
    length = len(sixteenNumber) - 1
    decimal = 0

    for index in sixteenNumber:
        if index in LETTER:
            index = LETTER.find(index)
            decimal += (int(index) * pow(16, length))
            length -= 1

    print(decimal)


# main
arraySixteenNumber = ['47', '127', 'AA']
for sixteenNumber in arraySixteenNumber:
    sixteenToDecimal(sixteenNumber)

