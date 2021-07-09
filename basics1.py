# Statements and expressions
# Statements are building blocks of a computer program:
a = 1
# Assigning a value to a variable is called an Assingnment statement.

# Example of for-statement/ a for-loop
for letter in ['a', 'b', 'c']:
    print(letter)


# Example 2:A for-loop is more powerful in a combinationwiht other statemants.
# Progrma printsout and count only vowels in a title in a poem:
# 'Say Not The Struggle Nought Availeth'
vowels = ('a', 'e', 'i', 'o', 'u')
title = 'Say Not The Struggle Nought Availeth'
count = 0
for letter in title:
    if letter in vowels:
        print(letter)
        count += 1
print(f"There are {count} vowels in '{title}'")
