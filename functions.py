# In Py, functions are defined using def keyword.
def message():
    print('My message.')

# Python allows defining functions on a single-line without indents:


def message(): print('My message.')


message()

# Define a function that executes multiple statements


def messages():
    print('My message.')
    print('My other message.')
    print('Something else.')


# Call this function
messages()

# Using return keyword to return values
# Functions help us print messages, execute a number of any Python statements in
# a row or do calculations in isolation. But they can also return a value or multiple
# values that can be later stored in a variable or printed.
# To return a value use the return statement and the value:


def thousand():
    return 1000


# Execcute the function
# and assing its return vlaue to variable num:
num = thousand()

print(num)
