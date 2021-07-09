# .........................Operators............................
# There are 7 different types of operators in Python: arithmetic,
# assignment, comparison, logical, identity, membership and bitwise.

# Assignment Operator
# Used to assign values to variables:
a = 10

# There are 7 different types of operators in Python: arithmetic, assignment, comparison, logical, identity, membership and bitwise.
three = [0, 0, 0]

# slice out 2 first items, replace with [1,1]
three[:2:] = [1, 1]

# Math operations
# Common math operations do exactly what you expect:
print(1 + 1)  # 2
print(5 - 2)  # 2
print(3 * 3)  # 2
print(8 / 2)  # 2

# ** Exponential operator
# Use the expononetial operator to riase a number int a powe of another value:
print(2**2)
print(2**3)

# // Floor division operator
# Return integral part of the quotient
print(6//2)
print(10//3)
print(12//3)

# % Modulus operator
# Return decimal part of quotient
print(6 % 2.5)
print(10 % 3.5)
print(12 % 3.5)

# Opposite to floor division, modulus returns the remainder component of a division.
# This is how much of the whole number on the right hand side of the operation did
# not fit into the number on the left hand side

# Assignment Operators
# += increment assignment
#  not limited to integers. It
# can be used on sequences (string, tuple and list) but not on dictionaries or sets:

# integer
a = 1
a += 1
print(a)

# string
s = 'ha'
s += 'ha'
print(s)

# turple
t = (1, 0)
t += (1, 2)
print(t)

# list
u = [1, 0]
u += [1, 2]
print(u)

# NB This will give an Error
# A set is a self-contained collection of items: for this reason it doesn’t
# share same qualities with the mutable type such as list
# Unlike list or tuple, set doesn’t allow duplicates. Items are not
# guaranteed to appear in the same order they were defined.
# Like tuple, the set data structure is immutable
# Sets are not subscriptable which means they cannot be accessed with [] operator.

# set

# v = {1, 0}
# v += {1}
# print(t)

# Items in a set are immutable – you cannot change them once they are added to the set. However, the elements of a set are mutable – which means you can still add or
# remove items (note that this still implies that no original value can be modified.)
# For example set.add(item) method adds one item to the set:

a = {1, 2}
a.add(3)

print(a)

# NB: Since sets dont have index, you can remove item by value.
a = {1, 2, 3, 4, 5}
a.remove(4)
print(a)

# Directories don't support += operator.
# But in latest version of python use |
d = {'a': 1}
c = {'b': 2}

print(d | c)
# You can also add directories using double star operators.
print({**d, **c})
# This wors similar to JS's spread operator.

# -= decreament assignment
# This operator will decrease the number by another number.
num = 10
num -= 4

print(num)

# /= multiplication assignment
num = 10
num *= 20
print(num)
