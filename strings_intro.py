# examples from introtopython.org

# strings are set off by quotes when assigned to a variable
# These can be double or single quotes
my_string = "This is a double-quoted string."
print(my_string)
my_string = 'This is a single-quoted string.'
print(my_string)

# To use quotes in a string you alternate the use of the single and double
# quotes
quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"
print(quote)

# examples of changing case of strings

first_name = 'eric'
print(first_name)
# capitalizes the first letter of all words in the string
print(first_name.title())
print(first_name.upper())  # capitalizes all letters in the string

first_name = "Eric"  # changing variable to include a capital letter for next change
print(first_name.lower())  # this changes the variable to all lower case.

# below is an example of concatenation of 2 strings
# and then the action "title" is used to capitalize the names.
first_name = 'ada'
last_name = 'lovelace'

full_name = first_name + ' ' + last_name

print(full_name.title())

# This block of code does the same but takes the name and combines it in a
# sentence.
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

message = full_name.title() + ' ' + \
    "was considered the world's first computer programmer."

print(message)

# Whitespace stripping, these do not affect the variable itself, just a
# copy of it that is being printed.
name = ' eric '

print(name.lstrip())  # removes leading whitespace only on copy of string
print(name.rstrip())  # removes trailing whitespace only on copy of string
print(name.strip())  # removes whitespace from both sides of the string

# in the code below, '-' dashes have been added to show more clearly what
# stripping does.
name = ' eric '

print('-' + name.lstrip() + '-')
print('-' + name.rstrip() + '-')
print('-' + name.strip() + '-')
