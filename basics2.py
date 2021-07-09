#
a = 9
b = a

fstring = f'{a + b} messages'

print (fstring)

a = 1 + 2 + 3 \
+ 4 + 5 + 6

print(a)


# line contnuation is preserved when defining lists on multiple lines
colors = ['red',
        'green', 
        'blue',
        'yellow'
]
# --------------------------------if STATEMENTS----------------------------------------
# If statements are used with an expression and another statement. 
#If the condition is met, then the statement that follows is executed

if True:
    print("Do something because it's true")

if False:
    print("Don't do this because condition is false something because it's true")
    print("Tghis text will never print to consoloe")

if 25 == 25:
    print('25 is 25')

if 5 * 5 == 25:
    print('5 * 5 is 25')


# -------------------------------- EXPRESSIONS--------------------------------------------
# Is a statement that produces a value (not all statemants result in a value).
# i.e an expression evaluates to a value.

1 + 1
# 1+1 is an expression that evaluates to 2.
# Although expresions produces a value, that value remains 'slient' untill its printed out

# Expressions can be used in maby different ways
a = 12 + 1
b = 10 / 5

print(a,b)

# We can use expressions directly as function arguments
print(1 + 4,
        10 * 2,
        'hello ' + 'there')

# A Python function that retruns a value can also be thought of as an expression
def func():
    return 'Gyebale'

msg = func()
print(msg) 

# ---------------------------------if-else-----------------------------------------------

video_is_playing = False

if video_is_playing:
    print('video is playing')
else:
    print('video is not playing')

# --------------------------------if and not-----------------------------------------------
# The 'not' keyword simply inverses the boolean condition. Similar to ! in other langauages 

video_is_playing = False

if not video_is_playing:
    print('video is not playing')
else:
    print('video is playing')

print(not True)
print(not False)

# -----------------------------------semi-colons------------------------------------------
# In most cases, Pyhton deosnt require semicolons. They can be used at the end of statements
# but mostly for optional aethetic and readability.
print('Hello');
# Satement same as,
print('Hello')

# However, there aer cases you might nrrrd a semi colon to seperate two or more statements on
# the same line:
print('a'); print('b'); print('c');
# NB print('a') print('b') print('c') wouldn't compile.