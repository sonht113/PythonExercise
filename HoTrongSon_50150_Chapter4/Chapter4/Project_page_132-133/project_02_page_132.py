"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_02_page_132.py
Problem:
    2.  Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a
        Caesar cipher. The script should work for any printable characters.

Solution:
    Display result
        Plain text =>  NOFOVYZOB
        Cipher text => DEVELOPER

"""

def caesar_cipher(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    result = ''

    for sym in message:
        if sym in LETTERS:
            num = LETTERS.find(sym)
            num = (num - key) % 26
            result += LETTERS[num]
        else:
            result += sym

    return result


message = ['NOFOVYZOB']

for text in message:
    output = caesar_cipher(text, 10)
    print('Plain text =>  ' + text)
    print('Cipher text => ' + output + '\n')


