"""
Author: Ho Trong Son
Date: 24/07/2021
Program: project_03_page_99.py

Problem:
    3.  Modify the guessing-game program of Section 3.5 so that the user thinks of a
        number that the computer must guess. The computer must make no more than
        the minimum number of guesses, and it must prevent the user from cheating by
        entering misleading hints. (Hint: Use the math.log function to compute the minimum
        number of guesses needed after the lower and upper bounds are entered.)

Solution:
"""
# Code here:

import math
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
limit = round(math.log(larger - smaller))

print("\nYou have", limit, "guesses")
while count < limit:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count,
              "tries!")
        break
    print("\nYou have", str(limit - count), "guesses left.")

# Result here:
# Enter the smaller number: 3
# Enter the larger number: 79
#
# You have 4 guesses
# Enter your guess: 5
# Too small!
#
# You have 3 guesses left.
# Enter your guess: 57
# Too small!
#
# You have 2 guesses left.
# Enter your guess: 56
# Too small!
#
# You have 1 guesses left.
# Enter your guess: 2
# Too small!
#
# You have 0 guesses lef