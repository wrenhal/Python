# This is from the video Python Programming by Derek Banas
# https://www.youtube.com/watch?v=N4mEzFDjqtA

print("Hello Python")

# This is a single line comment
'''
This is a multiline comment
We can type a second line here
'''
name = "Tony"
print(name)

# 5 datatypes we're gonna focus on
# Numbers, Strings, Lists, Tuples, and Dictionaries

# 7 different math operators
# + - * / % ** //
# add, subtract, multiply, divide, modulus, exponent, floor division
# modulus gives remainder of division
# floor division discards the remainder, basically rounding the answer down.

print('5 + 2 = ', 5 + 2)
print('5 - 2 = ', 5 - 2)
print('5 * 2 = ', 5 * 2)
print('5 / 2 = ', 5 / 2)
print('5 % 2 = ', 5 % 2)
print('5 ** 2 = ', 5 ** 2)
print('5 // 2 = ', 5 // 2)

# Multiplication and Division will be performed before
# Addition or Subtraction.  "Order Of Operations"

print('1 + 2 - 3 * 2 =', 1 + 2 - 3 * 2)
print('(1 + 2 - 3) * 2 =', (1 + 2 - 3) * 2)