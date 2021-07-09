# ----------------Printing Values--------
chickens = 10
print(chickens)  # prints 10 to commmand prompt

# --------------printing multiple values------------
# You can form multiple values by seperating vlaues by a comma:

num = 5
what = 'wolves'
print('there are', num, what)

# ---------Using {} placeholder and string's .format() method----------
# Objects of type string have a .format() method, making it possible to execute
# it directly on a string literal. Embedding empty curly braces {} into string creates
# a placeholder value specified in .format() method:

print('You have collected {} pine cones'.format(15))

# The number of {}’s must match the number of values passed into the .format()
# method as a comma separated list:

print('You have collected {} pine {}'.format(15, 'cones'))

# Both of the statements above will produce the same output.


# ----------Formatting Dynamic text values in proper English-----------
# For example: There ”are” 10 apple(s). But there ”is” 1 apple:
apples = 10
print('There are {} apples.'.format(apples))

apples = 1
print('There are {} apples.'.format(apples))

# One way of solving this problem is to use Python’s inline if/else statement:
cones = 15
letter = 's' if cones != 1 else ''
print('You have collected {} pine cone{}'.format(cones, letter))

cones = 1
letter = 's' if cones != 1 else ''
print('You have collected {} pine cone{}'.format(cones, letter))

# Previous example
apples = 1
letter = 's' if apples != 1 else ''
verb = 'are' if apples != 1 else 'is'
print('There {} {} apple{}'.format(verb, apples, letter))

apples = 200
letter = 's' if apples != 1 else ''
verb = 'are' if apples != 1 else 'is'
print('There {} {} apple{}'.format(verb, apples, letter))

# NB: the inline id=f/else statement evaluates based on provided condition.
# In this case we are testing the numeridc variable for not being equal to 1.
# And the linking verb for being either 'are' or 'is'
