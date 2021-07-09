# Every variable has 4 components: name, value, type and address.
# Variables are named placeholders for values that reside at a memory address

# How to find out variable's memory address.
# The built-in id function returns object identity – it’s the variable’s memory address
# in decimal format. If you run this on your computer, address will be different.
# Buit in id() function
a = 1
addr = id(a)
print(addr)


# Built-in hex() function
# ddresses are often displayed in hex format. To convert the object’s decimal
# identity to actual memory address you can use the hex() function which converts
# any integer (not just an address) into hexadecimal format.
a = 1
addr = id(a)
hexaddr = hex(addr)
print(addr)
print(hexaddr)
