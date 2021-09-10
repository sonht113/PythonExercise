"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_01_page_132.py
Problem:
    1. Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using
        a Caesar cipher. The script should work for any printable characters.

Solution:
    Display result
        Plain text =>  Developer
        Cipher text => NOFOVYZOB
"""

def caesar_cipher(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    result = ''

    for sym in message:
        if sym in LETTERS:
            num = LETTERS.find(sym)
            num = (num + key) % 26
            result += LETTERS[num]
        else:
            result += sym

    return result
message = ['Developer']

for text in message:
    output = caesar_cipher(text, 10)
    print('Plain text =>  ' + text)
    print('Cipher text => ' + output + '\n')

