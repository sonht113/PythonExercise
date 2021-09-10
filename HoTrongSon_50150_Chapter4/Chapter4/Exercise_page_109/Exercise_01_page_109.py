"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_01_page_109.py
Problem:
    1.  Write the encrypted text of each of the following words using a Caesar cipher with
        a distance value of 3:

        a.  python
        b.  hacker
        c.  wow

Solution:
    Display result:

        Plain item:  python
        Cipher item: GPKYFE

        Plain item:  hacker
        Cipher item: YRTBVI

        Plain item:  wow
        Cipher item: NFN

"""
#Code here:
def caesar_cipher(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    result = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = (num + key) % 26
            result += LETTERS[num]
        else:
            result += symbol

    return result


message = ['python', 'hacker', 'wow']

for item in message:
    cipher = caesar_cipher(item, 17)
    print('Plain item =>  ' + item)
    print('Cipher item => ' + cipher + '\n')
