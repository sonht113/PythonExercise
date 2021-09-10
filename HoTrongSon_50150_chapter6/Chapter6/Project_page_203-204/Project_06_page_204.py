"""
Author: Ho Trong Son
Date: 05/09/2021
Program: Project_06_page_204.py
Problem:
    6.  Add a command to this chapter’s case study program that allows the user to view the contents of a file in
        the current working directory. When the command is selected, the program should display a list of filenames
        and a prompt for the name of the file to be viewed. Be sure to include error recovery.

Solution:
"""
# Code here:
import os, os.path

QUIT = '8'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7', '8')
MENU = """
1 List the current directory.
2 Move up.
3 Move down.
4 Number of files in the directory.
5 Size of the directory in bytes.
6 Search for a filename.
7 View the contents of a file.
8 Quit the program.
"""


def listCurrentDir(dirName):
    list = os.listdir(dirName)
    for element in list:
        print(element)


def moveUp():
    os.chdir("..")


def moveDown(currentDir):
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")


def countBytes(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count


def findFiles(target, path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
            else:
                os.chdir(element)
                files.extend(findFiles(target, os.getcwd()))
                os.chdir("..")
    return files


def countFiles(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count


def view_file():
    print(f"File in {os.getcwd()}: ")
    for file_name in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), file_name)):
            print(file_name)

    in_file = input("Enter a file name from these names: ")
    if os.path.isfile(in_file):
        f = open(in_file, "r")
        print(f.read())
    else:
        print("File not exists!")
        view_file()


def acceptCommand():
    command = input("Enter a number: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: command not recognized")
        return acceptCommand()


def runCommand(command):
    if command == "1":
        listCurrentDir(os.getcwd())
    elif command == "2":
        moveUp()
    elif command == "3":
        moveDown(os.getcwd())
    elif command == "4":
        print("The total number of files is", countFiles(os.getcwd()))
    elif command == "5":
        print("The total number of bytes is", countBytes(os.getcwd()))
    elif command == "6":
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    elif command == "7":
        view_file()


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
