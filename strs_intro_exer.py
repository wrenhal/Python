# String Exercises for introtopython.org

quote = 'A quote from the Bible that I like: "If it is disagreeable in your sight to serve the Lord, choose for yourselves today whom you will serve: whether the gods which your fathers served which were beyond the River, or the gods of the Amorites in whose land you are living; but as for me and my house, we will serve the Lord."'
print(quote)

first_name = 'tony'
print(first_name) # prints string as listed originally
print(first_name.title()) # prints string with first letter capital
print(first_name.upper()) # prints string in all upper case

# storing full name in separate variables to concatenate and print
first_name = 'tony'
last_name = 'lettkeman'
print(first_name.title() + ' ' + last_name.title())

first_name = 'tony'
last_name = 'lettkeman'
print(first_name.title() + ' ' + last_name.title() + ' is a pretty stand up guy.')

name = '   Tony  '

print('-' + name + '-') # printing name as is
print('-' + name.lstrip() + '-') # printing name with leading whitespace stripped
print('-' + name.rstrip() + '-') # printing name with trailing whitespace stripped
print('-' + name.strip() + '-') # printing name with all whitespace stripped