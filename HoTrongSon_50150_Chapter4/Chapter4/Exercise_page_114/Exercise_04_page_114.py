"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_04_page_114.py
Problem:
    4.  Translate each of the following numbers to decimal numbers:
        a.  47(8)
        b.  127(8)
        c.  64(8)

Solution:
    Result:
        a.  39
        b.  87
        c.  52

"""

def eightToDecimal(eightNumber):
    length = len(eightNumber)
    eightNumber = int(eightNumber)
    decimal = 0
    for i in range(0, length):
        index = eightNumber % 10
        decimal += (index * pow(8, i))
        eightNumber //= 10

    print(decimal)


# main
arrayEightNumber = ['47', '127', '64']
for eightNumber in arrayEightNumber:
    eightToDecimal(eightNumber)
