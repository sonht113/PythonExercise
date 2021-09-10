"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_07_page_133.py
Problem:
    7.  Write a script that decrypts a message coded by the method used in Project 6

Solution:
    Display result
        Enter a text: 1101001 1100001 1011111
        son
"""

def textToDecimal(text):
    if len(text) > 1:
        text = text[-1] + text[:-1]
    decimal = 0
    ex = len(text) - 1
    for digit in text:
        decimal = decimal + int(digit) * 2 ** ex
        ex = ex - 1
    return decimal

Text = input("Enter a text: ")

bit = Text.split()
textString = ''
for text in bit:
    textString += chr(textToDecimal(text) - 1)

print(textString)
