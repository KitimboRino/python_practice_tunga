# Programme to  Convert kilometers to Miles

# Initialize to a non numeric value
kilometers = ''

# while not loop to shift numeric values
while not kilometers.isnumeric():
    kilometers = input('Enter the number of kilometers:')

# Convert Km to floating point number
kilometers = float(kilometers)

# km/mi conversion factor
factor = 0.621371

# determinie miles from kilometers
miles = kilometers * factor

# print result in commandline
print('%0.2f km = %0.2f mi' % (kilometers, miles))
