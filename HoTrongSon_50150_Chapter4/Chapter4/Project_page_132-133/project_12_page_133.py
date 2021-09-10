"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Project_12_page_133.py
Problem:
    12. The Payroll Department keeps a list of employee information for each pay period in a text file.
        The format of each line of the file is the following:
                                <last name> <hourly wage> <hours worked>
        Write a program that inputs a filename from the user and prints to the terminal a report of the
        wages paid to the employees for the given period. The report should be in tabular format with
        the appropriate header. Each line should contain an employee�s name, the hours worked, and the
        wages paid for that period.

Solution:
    Display result
        Enter the file name: ../textFile/project12.txt
        Name                Hours Work           Total Pay
        Ho                          10               135.0
        Dang                        15              123.75
        Tran                         7                86.8

"""

fileName = input("Enter the file name: ")

inputFileName = open(fileName, 'r')

print("%-20s%10s%20s" % ("Name", "Hours Work", "Total Pay"))
for line in inputFileName:
    dataList = line.split()
    name = dataList[0]
    hoursWork = int(dataList[1])
    moneyPriceOneHour = float(dataList[2])
    totalPay = hoursWork * moneyPriceOneHour
    print("%-20s%10s%20s" % (name, hoursWork, totalPay))
