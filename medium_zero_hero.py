# This is my combination of all the examples from the following page:
# https://medium.freecodecamp.org/learning-python-from-zero-to-hero-120ea540b567


# if elif and else examples
if 1 > 2:
    print("1 is greater than 2")
elif 2 > 1:
    print("1 is not greater than 2")
else:
    print("1 is equal to 2")

# while and for looping examples
num = 1

while num <= 10:
    print(num)
    num += 1

loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" % (loop_condition))
    loop_condition = False

for i in range(1, 11):
    print(i)

# list examples
my_integers = [5, 7, 1, 3, 4]
print(my_integers[0])  # 5
print(my_integers[1])  # 7
print(my_integers[4])  # 4

relatives_names = [
    "Toshiaki",
    "Juliana",
    "Yuji",
    "Bruno",
    "Kaio"
]

print(relatives_names[4])  # Kaio

# how to add an item to a list using append
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0])  # The Effective Engineer
print(bookshelf[1])  # The 4 Hour Work Week

# how to iterate through a list
bookshelf = [
    "The Effective Engineer",
    "The 4 hours work week",
    "Zero to One",
    "Lean Startup",
    "Hooked"
]

for book in bookshelf:
    print(book)

# dictionary examples
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian"
}

print("My name is %s" % (dictionary_tk["name"]))  # My name is Leandro
print("But you can call me %s" %
      (dictionary_tk["nickname"]))  # But you can call me Tk
print("And by the way I'm %s" % (dictionary_tk["nationality"]))

dictionary_tk['age'] = 24  # adding a key:value pair

# ways to iterate through a dictionary

print(dictionary_tk)

for key in dictionary_tk:
    print(key)  # prints just the key without it's value

for tk_values in dictionary_tk.items():
    print(tk_values)  # prints the key and it's corresponding value

# iterate through the dictionary and adding the key/value pairs
# as parameters to a printed string statement
for attribute, value in dictionary_tk.items():
    print("My %s is %s" % (attribute, value))

# example of OOP.  Designation of class


class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print('VRUUUUUUUM')


@property
def number_of_wheels(self):
    return self.number_of_wheels


@number_of_wheels.setter
def number_of_wheels(self, number):
    self.number_of_wheels = number


tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels)  # 4
tesla_model_s.number_of_wheels = 2  # setting number of wheels to 2
print(tesla_model_s.number_of_wheels)  # 2
tesla_model_s.make_noise()  # VRUUUUUUUM

