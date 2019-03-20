#!/usr/bin/env python3

# That's how you should write a comment

""" Or in this form
    if you need multiple lines
"""

# So now, you can describe your code as you want

# And I will use the comments to describe the further lessons


# if you execute :
#   $ python 01-basics/02-syntax.py

# you will see "Hello world !" in the output
# because of this line
print('Hello world !')

# you can set variables like this
x = 'a'
y = 2
z = 'c'
i = 'd'

# and concatenate them in the output
# like this
print('r1 : %s %d' % (x, y))

# %s for 'strings'
# and %d for 'decimals'

# or like this, that is less recommended for readability
# and only works for strings
# but you must know both writings exist
print('r1 : ' + z + ' ' + i)


# At this point, you should yet consider to use a "linter"
# That's a program that sets rules about code writing
# and ensures they are respected in your code

# You can install pylint, and check your file is complient
#  $ pip install pylint
#  $ pylint 01-basics/02-syntax.py

# You can refer to the PEP8 coding standards
# https://www.python.org/dev/peps/pep-0008/

# and eventually set exceptions
# on files with : `#pylint disable ..options`
# or on projects with a `.pylintrc` file
# all exceptions are described here : https://pylint.org/
# or here : https://pep8.readthedocs.io/en/latest/intro.html#configuration

# The best option would be to install a pylint checker on your favorite text editor or IDE
# to check direclty if the code don't follow the rule you want
# for instance for VSCode : https://code.visualstudio.com/docs/python/linting


# That's it, now you can continue the next lessons
