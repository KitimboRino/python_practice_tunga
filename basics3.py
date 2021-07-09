# Simple program
# One difference btn Pythin and other languages is that the absence of
# curly brackets when deffinfing a block of code. In this case, the body of the
# while loop is indented by 4 spaces.
# You can use any number of characters/ tabs as long as they are consistent with the 
# previous line in the same block scope.
# The while c: statement is evaluated to True as long as c remains a positive number. 
# Then c is decremented by 1 by executing c -= 1 statement. 
# When c reaches 0 while loop will interpret it as False
# and terminate. The result is 3 decreasing numbers printed in a row.

c = 3
while c:
    print(c)
    c -= 1

# Another program that picks random numbers from a range.
# mport keyword the program includes a built-in module called random. 
# This package contains methods for working with random numbers.
# The random.choice method returns a random element from a set. 
# In Python ordered sets of items can be also referred to as sequences.
# The built-in range function generates a linear set of numbers between 1 and 15.
# This sequence is then stored in the variable numbers.
# The script then creates a variable called chosen to store an empty array [].
# Inside the while loop a random number is chosen and stored in number variable.
# numbers.remove(number) line removes that number from numbers sequence.
# Then it will append the same number to chosen array.
# This is equivalent to moving it from numbers array into chosen array.
# Without a condition while loop iterates infinitely. But because it checks length
# of the array chosen using another built-in Python method len, when the length
# of chosen array reaches 6 the loop will be terminated.
# Lastly, using built-in print function, we output the array chosen. It will contain 6
# numbers randomly picked out from the original range that was stored in numbers.
# If you run it, the result of this program will be printed to the console:

import random

numbers = range(1, 15)
chosen = []

while len(chosen) <6:
    number = random.choice(numbers)
    chosen.append(number)

print(chosen)

# NB: Don't name your Python files the same name as built-in Python modules.

#---------- Python poem example--------
# This script should save lives
# import soul

# for days in len(life)
#     print 'happiness'

# Running Python Scripts
# Python scripts are usually saved in files ending with .py extension.
# To execute the script { python filename.py} or {pyhon filename}

# -------------Comments-----------------
# Every time you see # character in Python code it indicates a comment. Comments
# are useful for documenting your code:

# create variable a and assign 1 to it
# a = 1
# Comments can trail after the statement:
# E.g print(message) # Print my message

# -------------- An early exit----------
# You can exit your Python script early and abandon executing any of the following
# commands after the exit() function:

print('This message will print')
exit()
print("This message won't.")
# Because we exited the script with built in exit() only the first statement was
# executed. You can use exit() anywhere in your program
