#!/usr/bin/env python3

# you can write text surrounded by "" or ''
text = "This is a test"
print(text)

print(type(text))
#   <class 'str'>


# here are some usual functions for strings

# len : get the length of the string
print(len(text))

# upper : for uppercase
print(text.upper())

# lower : for lowercase
print(text.lower())

# strip : removes whitespaces around the text
print("     x     ".strip())

# substring : returns a portion of the string
print(text[5:7])

# replace : replaces a part of the string by another
print(text.replace("test", "proof of concept"))

# split : splits the string to a list of substrings
print(text.split(" "))
print(type(text.split(" ")))
