"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_08_page_133.py
Problem:
    8.  Write a script named copyfile.py. This script should prompt the user for the names of two text files.
        The contents of the first file should be input and written to the second file.

Solution:
    Display result
        Enter the input file name: ../textFile/project8.txt
        Enter the output file name: ../textFile/test8.testproject8.text
"""

inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")

inputFile = open(inputFileName, 'r')
text = inputFile.read()

outFile = open(outputFileName, 'w')
outFile.write(text)
outFile.close()
