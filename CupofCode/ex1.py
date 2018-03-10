print('Since this string is in quotes and tied to the print function, python knows to "print" it on the screen')
x = 9 # assigns 9 to x
x = 15 # changes x to 15
# None of the following lines change the value assigned to x
# These only use the value in arithmetic.
print(x) # 15
print(x+2) # 17
print(x**2) # 225
print(x/2) # 7.5
print(x//2) # 7 

x = 'two ' # space added after the word so that there is a space between the outputs.
y = 'three'

print(x+y)

ln1 = 'I will start the line here... '
ln2 = ' and finish the line here '
ln3 = ln1+ln2

print(ln3)
print(ln3+ln3)

print('"this is a test"') # shows the ability to print quotes in a string.  