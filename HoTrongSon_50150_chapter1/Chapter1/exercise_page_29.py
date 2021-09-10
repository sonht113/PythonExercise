
# Author:  Ho Trong Son
# Date: 06/07/2021
# Program: exercise_page_29.py
# PROBLEM:
#     1. Describe what happens when the programmer enters the string "Greetings!" in
#     the Python shell.
#     2. Write a line of code that prompts the user for his or her name and saves the user’s
#     input in a variable called name.
#     3. Answer the question, What is a Python script?
#     4. Explain what goes on behind the scenes when your computer runs a Python program

# SOLUTION:
#     1)
#       print("Greetings!")
#       OR
#       T = "Greetings!"
#       print(T)

#     2)
#       name = input("Please!!! Enter your name: ")
#       print(name)

#     3)
#       It's a language that Python already knows,
#       so when certain words are input into Python like "for" Python already knows the significance of "for".

#     4)
#       When a Python program is executed:
#       - The interpreter reads a Python expression or statement, also called the source
#          code , and verifies that it is well formed. As soon as the interpreter encounters such an error,
#          it halts translation with an error message.

#       - If a Python expression is well formed, the interpreter then translates it to an equiva-
#         lent form in a low-level language called byte code .

#       - This byte code is next sent to another software component, called the Python
#         virtual machine (PVM) , where it is executed. If another error occurs during this
#         step, execution also halts with an error message.