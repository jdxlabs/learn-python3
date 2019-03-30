#!/usr/bin/env python3

# That's how you should write a comment

""" Or in this form
    if you need multiple lines
"""

# so now, you can describe your code as you want

# and I will use the comments to describe the further lessons


# if you execute :
#   $ python3 01-basics/02-syntax.py

# you will see "Hello world !" in the output
# because of this line
print("Hello world !")

# you can set variables like this
x = "a"
y = 2
z = "c"
i = "d"

# and concatenate them in the output like this
print("r1 : {} {}".format(x, y))

# you can also concatenate like this
print("r1 : %s %d" % (x, y))
# %s for "strings"
# and %d for "decimals"

# or like this, that is less recommended for readability
# and concatenation only works for strings (for numbers, it makes obviously additions)
print("r1 : " + z + " " + i)

# for better explanation about concatenation
# you can refer to this excellent article :
# https://realpython.com/python-string-formatting/#4-template-strings-standard-library


# You can execute the files, by typing :
#   $ python <my-file>.py

# or execute the code in the interpreter, by just typing :
#   $ python

# You can experiment by writing and modifying the code by yourself.


# At this point, you should yet consider to use a "linter"
# That's a program that sets rules about code writing
# and ensures they are respected in your code

# You can install pylint, and check your file is compliant
#  $ pip3 install pylint
#  $ pylint 01-basics

# When you will create python modules, you can launch the command like that
#  $ pylint <folder-or-file-name-for-my-modules> --ignore <some>,<folders>

# Pylint refers to the PEP8 coding standards
# https://www.python.org/dev/peps/pep-0008/

# You can eventually set exceptions
# on files with : `#pylint disable ..options`
# or on projects with a `.pylintrc` file
# all exceptions are described here : https://pylint.org/
# or here : https://pep8.readthedocs.io/en/latest/intro.html#configuration

# The best option would be to install a pylint checker on your favorite text editor or IDE
# to check directly if the code don't follow the rule you want
# for instance for VSCode : https://code.visualstudio.com/docs/python/linting
# or PyCharm : https://plugins.jetbrains.com/plugin/11084-pylint


# That's it, now you can continue to the next lessons !
