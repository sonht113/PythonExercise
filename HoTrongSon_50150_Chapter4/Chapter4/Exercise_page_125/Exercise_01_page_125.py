"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_01_page_125.py
Problem:
    1.  Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file.

Solution:
    Display result:
        Content first 2 characters: Ho

"""

textFile = open("../textFile/myfile.txt", 'w', encoding='utf-8')
textFile.write("Ho Trong Son")

textFile = open("../textFile/myfile.txt", 'r', encoding='utf-8')
print("Content first 2 characters:", textFile.read(2))

textFile.close()



