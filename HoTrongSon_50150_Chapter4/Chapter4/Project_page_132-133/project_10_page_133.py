"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_10_page_133.py
Problem:
    10. Write a script named dif.py. This script should prompt the user for the names of two text files and compare
        the contents of the two files to see if they are the same. If they are, the script should simply output "Yes".
        If they are not, the script should output "No", followed by the first lines of each file that differ from each
        other. The input loop should read and compare lines from each file. The loop should break as soon as a pair
        of different lines is found.

Solution:
    Display result
        Enter the first file name: ../textFile/project8.txt
        Enter the second file name: ../textFile/textproject9.txt
        No
        Ho Trong Son
        1> Ho Trong Son

"""

fileName1 = input("Enter the first file name: ")
fileName2 = input("Enter the second file name: ")

inputFile1 = open(fileName1, 'r')
inputFile2 = open(fileName2, 'r')

while True:
    lineFile1 = inputFile1.readline()
    lineFile2 = inputFile2.readline()
    if lineFile1 == "" and lineFile2 == "":
        print("Yes")
        break
    elif lineFile1 != lineFile2:
        print("No")
        print(lineFile1)
        print(lineFile2)
        break
