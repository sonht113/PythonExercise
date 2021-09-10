"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_02_page_109.py
Problem:
    2.  Consult the Table of ASCII values in Chapter 2 and suggest how you would modify the encryption and
        decryption scripts in this section to work with strings containing all of the printable characters.

Solution:
    Display result:
        Plain item =>  python
        Cipher item => ÔÝØÌÓÒ

        Plain item =>  hacker
        Cipher item => ÌÅÇÏÉÖ

        Plain item =>  wow
        Cipher item => ÛÓÛ


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


message = ['python', 'hacker', 'wow']

for item in message:
    cipher = caesar_cipher(item, 'ENCRYPT', 100)
    print('Plain item =>  ' + item)
    print('Cipher item => ' + cipher + '\n')

