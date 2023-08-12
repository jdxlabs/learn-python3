#!/usr/bin/env python3

# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    # method
    def has_birthday(self):
        self.age += 1

# extend class
class Customer(User):
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # add property
        self.balance = 0

    # method
    def set_balance(self, balance):
        self.balance = balance

    # method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# init user object
brad = User('Brad Traversy', '37')
brad.has_birthday()
print(brad.greeting())
#   My name is Brad Traversy and I am 37

# init customer object
janet = Customer('Janet Johnson', '25')
janet.set_balance(500)
print(janet.greeting())
#   My name is Janet Johnson and I am 25 and my balance is 500
# call method
brad.has_birthday()
