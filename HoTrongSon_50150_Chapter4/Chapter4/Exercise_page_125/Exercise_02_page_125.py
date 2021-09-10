"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_02_page_125.py
Problem:
    2.  Write a code segment that opens a file for input and prints the number of four-letter words in the file.


Solution:
    Display result:
        Content first 4 characters: Ho T

"""

textFile = open("../textFile/myfile.txt", 'w', encoding='utf-8')
textFile.write("Ho Trong Son")

textFile = open("../textFile/myfile.txt", 'r', encoding='utf-8')
print("Content first 4 characters:", textFile.read(4))

textFile.close()
