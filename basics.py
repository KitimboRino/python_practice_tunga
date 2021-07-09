# Type constryctor functions: int(), float(), str(),  complex(), tuple(), list()
# Each creates a primitive object of that type.

# Integer
integer = 125
print(integer)

# Convert to decimal number
decimal = float(integer)
print(decimal)

# Convert decimal back to wholw number
whole = int(decimal)
print(whole)

# Boolean: type constructor bool()
yes = True
no = False

print(yes)
print(no)

# Initialize a boolean with one of its own values.
print(bool(True))
print(bool(False))

# Initialize a boolean with a number or string.
print(bool(0))
print(bool(1))
print(bool(''))

print(bool(''))
print(bool('0'))
print(bool('Hello'))
print(bool(1))
print(bool(125))
print(bool(-1))
print(bool(0))


# Checking the type of the value by using Python's built-in type function
yes = True
no = False
n = 1
s = 'Hello there'

a = type(yes)
b = type(no)
c = type(n)
d = type(s)

print(a)
print(b)
print(c)
print(d)

