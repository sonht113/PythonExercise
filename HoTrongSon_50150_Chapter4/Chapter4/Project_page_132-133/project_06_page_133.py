"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_06_page_133.py
Problem:
    6.  Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5
        to code a new encryption algorithm. The algorithm should add 1 to each character’s numeric ASCII value,
        convert it to a bit string, and shift the bits of this string one place to the left. A single-space
        character in the encrypted string separates the resulting bit strings.

Solution:
    Display result
        Enter a message: son
        1101001 1100001 1011111
"""

Text = input("Enter a message: ")

result = ''

for item in Text:
    ordValue = ord(item) + 1

    string = ''
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        string = str(remainder) + string

    if len(string) > 1:
        string = string[1:] + string[0]

    result += string + " "

print(result)
