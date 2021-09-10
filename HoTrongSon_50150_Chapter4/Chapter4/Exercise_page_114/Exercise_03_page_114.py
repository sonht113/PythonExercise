"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_03_page_114.py
Problem:
    3.  Translate each of the following numbers to binary numbers:
        a.  47(8)
        b.  127(8)
        c.  64(8)

Solution:
    Result:
        a.  100111
        b.  110111
        c.  110100

"""
def eightToBit(number):
    bitString = ''
    number = str(number)
    for num in number:
        num = int(num)
        if(num == 0):
            print(0)
        else:
            bitStringNum = ''
            while (num > 0):
                surplus = num % 2
                num = num // 2
                bitStringNum = str(surplus) + bitStringNum
            bitString += bitStringNum
    print(bitString)

arrayEightNumber = [47, 127, 64]
for eightNumber in arrayEightNumber:
    eightToBit(eightNumber)