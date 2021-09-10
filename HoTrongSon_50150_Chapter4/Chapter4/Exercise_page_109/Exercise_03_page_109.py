"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_03_page_109.py
Problem:
    3.  You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can
        contain any of the printable ASCII characters. Suggest an algorithm for cracking this code.

Solution:
    Display result:
        Plain item =>  ÔÝØÌÓÒ
        Cipher item => python

        Plain item =>  ÌÅÇÏÉÖ
        Cipher item => hacker

        Plain item =>  ÛÓÛ
        Cipher item => wow

"""

def caesar_cipher(message, mode, key):
    result = ''

    for symbol in message:
        number = ord(symbol)
        if mode.upper() == 'ENCRYPT':
            number = (number + key) % 256
        elif mode.upper() == 'DECRYPT':
            number = (number - key) % 256
        result += chr(number)
    return result


message = ['ÔÝØÌÓÒ', 'ÌÅÇÏÉÖ', 'ÛÓÛ']

for item in message:
    cipher = caesar_cipher(item, 'DECRYPT', 100)
    print('Plain item =>  ' + item)
    print('Cipher item => ' + cipher + '\n')

