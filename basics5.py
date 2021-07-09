# ------The .format() method automatically interpretes value by type
# By default the .format() method will automatically interpret either numeric or
# string variables with respect to the type of variable’s value.
# Whole floating point numbers will be reduced to one trailing zero:

print('num = {} '.format(15.0000))  # prints 15.0

# a proper number of trailing zeros will be dispayed fr non-0 decimalpoint:

print('num = {}'.format(15.0025))  # prints 15.0025


# --------FLoating point and .format() method
# sing {:.f} will force the value to be interpreted as floating point number
# regardless of whether it actually is (in this case it’s a whole number):

print('Your balance is ${}f'.format(125))


# --------FLoating Point with decima point----------
#  you want to choose number of digits to the right of . in a floating point number.
#  For example, when displaying financial information like balance.
# You can do that with {:.2f}

num = 125
print("Your balance is Ugx{}:.2f".format(num))


# ---------Using % Value Interpretation character...........
# You can also print one or multiple variables with print function by using %
# character embedded directly into the target string:

num = 12
what = 'foxes'
print('There are %i %s' % (num, what))

# Above, %i placeholder will interprete the value as an integer (int).
# The %s placeholder will interprete the value as a string (str).
# Actual values are provided after % separator usually in parentheses.
# In Python 2.9 or less there are no parentheses:
# chickens = 15
# print chickens # prints 15 to command prompt
# (This is illegal in 3.0 and up, but still nice to know for legacy code.


# --------------------Conditions------------------
# Python provides a set of operators for comparing values based on logical conditions.
print(15 == 15)
print(15 != 10)
print(10 < 23)
print(15 <= 10)
print(3 > 8)
print(16 >= 14)


# -----------------if and if..else statements.............
a = 100
b = 200

if b > a:
    print('b is greater than a')
else:
    print('b is lesser or equal to a')
