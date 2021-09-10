"""
Author: Ho Trong Son
Date: 5/08/2021
Program: Exercise_05_page_125.py
Problem:
    5.  Write a code segment that prompts the user for a filename. If the file exists, the program should print
        its contents on the terminal. Otherwise, it should print an error message.
Solution:
    Display result:
    
        Enter name file: Exercise_01_page_125.py
        AUTHOR: HO TRONG SON
        DATE: 5/08/2021
        PROGRAM: EXERCISE_01_PAGE_125.PY
        PROBLEM:
            1.  WRITE A CODE SEGMENT THAT OPENS A FILE NAMED MYFILE.TXT FOR INPUT AND PRINTS THE NUMBER OF LINES IN THE FILE.

        SOLUTION:
            DISPLAY RESULT:
                CONTENT FIRST 2 CHARACTERS: HO

        TEXTFILE = OPEN("../TEXTFILE/MYFILE.TXT", 'W', ENCODING='UTF-8')
        TEXTFILE.WRITE("HO TRONG SON")

        TEXTFILE = OPEN("../TEXTFILE/MYFILE.TXT", 'R', ENCODING='UTF-8')
        PRINT("CONTENT FIRST 2 CHARACTERS:", TEXTFILE.READ(2))

        TEXTFILE.CLOSE()
        
"""

fileName = input("Enter name file: ")

try:
    fn = open(fileName)
except:
    print('Cannot open the file ', fileName, 'try again!!!')
    quit()

for line in fn:
    line = line.upper()
    line = line.rstrip()
    print(line)

