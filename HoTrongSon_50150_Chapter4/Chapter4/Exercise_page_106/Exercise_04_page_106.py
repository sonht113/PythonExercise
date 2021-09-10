"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_04_page_106.py
Problem:
    4.  Assume that the variable myString refers to a string, and the variable reversedString refers to an empty
        string. Write a loop that adds the characters from myString to reversedString in reverse order.

Solution:
    Display result:
        n o s a J

"""
#Code here:
string = 'Jason'
reversedString = ''

length = len(string)
for index in range(length - 1, -1, -1):
    reversedString += string[index] + ' '

print(reversedString)

