"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_03_page_132.py
Problem:
    3.  Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.

Solution:
    Display result
        Plain text =>  NOFOVYZOB
        Cipher text => DEVELOPER

"""

def caesar_cipher(message, mode, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    result = ''

    for sym in message:
        if sym in LETTERS:
            num = LETTERS.find(sym)
            if mode.upper() == 'ENCRYPT':
                num = (num + key) % 26
            elif mode.upper() == 'DECRYPT':
                num = (num - key) % 26
            result += LETTERS[num]
        else:
            result += sym

    return result


message = ['NOFOVYZOB']

for item in message:
    output = caesar_cipher(item, 'DECRYPT', 10)
    print('Plain text =>  ' + item)
    print('Cipher text => ' + output + '\n')
