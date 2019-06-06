#!/usr/bin/env python3

x = 1
y = 2
z = 3
i = 1.2
j = 3j
k = -4

print(x)

print(type(x))
#   <class 'int'>

print(type(i))
#   <class 'float'>

print(type(j))
#   <class 'complex'>

print(type(int(i)))
# float casted to int :
#   <class 'int'>

print(type(float(x)))
# int casted to float :
#   <class 'float'>

print(type(True))
# booleans are True or False
#   <class 'bool'>


# Arithmetic operators

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
print(x / y)

# Modulus
print(x % y)

# Exponentiation
print(x ** y)

# Floor division
print(x // y)


# Assignment operators

# Equality
x = y

# You can write addition like this
x += y
# This is a shorter writing of
#   x = x + y

# You can do the same with other arithmetic operators
x -= y
x *= y
x /= y
x %= y
x **= y
x //= y


# Comparison operators

# Equal
print(x == y)

# Not equal
print(x != y)

# Greater than
print(x > y)

# Less than
print(x < y)

# Greater than or equal to
print(x >= y)

# Less than or equal to
print(x <= y)


# Logical operators

# Returns True if both statements are true
print(x and y)

# Returns True if one of the statements is true
print(x or y)

# Reverse the result, returns False if the result is true
print(not x)


# Identity operators

# Returns true if both variables are the same object
print(x is y)

# Returns true if both variables are not the same object
print(x is not y)


# Bitwise operators

# This operators act on operands as if they were string of binary digits.
# It operates bit by bit, hence the name.
# For example, 2 is 10 in binary and 7 is 111.
x = 4
y = 10

# Bitwise AND
print(x & y)

# Bitwise OR
print(x | y)

# Bitwise XOR
print(x ^ y)

# Bitwise right shift
print(x >> y)

# Bitwise left shift
print(x << y)
