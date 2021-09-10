"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_03_page_125.py
Problem:
    3.  Assume that a file contains integers separated by newlines. Write a code segment that opens the
        file and prints the average value of the integers.

Solution:
    Display result:
        Average: 5.0

"""
#Code here:
textFile = open("../textFile/myfile.txt", 'w', encoding='utf-8')
for index in range(1, 50):
    textFile.write(str(index) + '\n')

textFile = open("../textFile/myfile.txt", 'r', encoding='utf-8')
sum = 0
count = 0
for line in textFile:
    sum += int(line.strip())
    count += 1
    print(sum)
average = sum/count

print("Average =>", average)
