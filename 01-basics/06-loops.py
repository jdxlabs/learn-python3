#!/usr/bin/env python3

# you can use the while loop
# be carrefull to not create infinite loops with it
x = 1
while x <= 3:
    print(x)
    x += 1

# # you can use the break statement
# to conditionnaly exit the loop
x = 1
while x <= 3:
    print(x)
    if x == 1:
        break
    x += 1

# or the continue statement
# to conditionnaly go to the next iteration of the loop
x = 1
while x <= 20:
    x += 1
    if x % 2 == 0: # is pair
        continue
    print(x)

# you can use the for loop
items = ["pears", "apples", "bananas"]
for item in items:
    print(item)

# break and continue statements
# can be used in the for loop too

# The range() function returns a sequence of numbers, starting from 0
for x in range(3):
    print(x)

# however it is possible to specify the starting value by adding a parameter
for x in range(10, 15):
    print(x)

# range allows you to define to define the incrementation
# with the third parameter, here is an increment of 5
for x in range(10, 25, 5):
    print(x)

# you can use the else statement with the for loop
# complementary to the break statement
for x in range(3):
    if x == 30:
        break
    print(x)
else:
    print("not catched by the break statement")
