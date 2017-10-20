# from introtopython.org

# Integers
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3**2)

# modifying the standard order of operations
standard_order = 2 + 3 * 4  # 3*4 first then add 2
print(standard_order)  # answer 14

# add parentheses to change the order
my_order = (2 + 3) * 4  # this has 2+3 first then multiply by 4
print(my_order)

# Floating Points
print(0.1 + 0.1)  # normal example
print(0.1 + 0.2)  # unexpectedly long answer
print(3 * 0.1)  # also unexpectedly long

# Division in Python 3.x always delivers a decimal based float
print(4 / 2)  # 2.0 is the 3.x answer.  In Python 2.x the answer is simply 2
print(3 / 2)  # 1.5 is the 3.x answer.  In 2.x the answer is simply 1
