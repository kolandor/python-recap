# Loops allow you to perform some action depending on the satisfaction of some condition. 
# Python has the following types of loops

# Loop while
# A while loop tests the truth of some condition, and if the condition is true,
# it executes the statements of the loop. It has the following formal definition:
# while conditional_expression:
#  instructions
# [else
#  else instructions]

# Example
iterator = 0
count = 5
print(f"'while' example expression: {iterator} < {count}")
while iterator < 5:
    print(f"In loop iterator: {iterator}")
    iterator += 1
print(f"'while' loop ended, iterator = {iterator}\n")

# !!!Python feature
# For a while loop, you can also define an additional else block 
# whose statements are executed when the condition is False:

iterator = 0
count = 5
print(f"'while' example expression: {iterator} < {count}")
while iterator < 5:
    print(f"In loop iterator: {iterator}")
    iterator += 1
else:
    print(f"While loop expression false, iterator = {iterator}")
print("'while' loop ended\n\n")

# Loop for
# Another type of loop is the for construct.
# This loop iterates through a set of values, puts each value into a variable,
# and then in the loop we can do various things with that variable.

# !!!Python for works like foreach in most other languages

# Formal definition of a for loop:
# for variable in value_set:
#  instructions
# [else
#  else instructions]

# Example
msg = "Hello"
print(f"'for' loop example, string = {msg}")
for char in msg:
    print(f"Iferation char: {char}")
print("'for' loop ended\n")

msg = "Hello!"
print(f"'for' loop example with 'else' block, string = {msg}")
for char in msg:
    print(f"Iferation char: {char}")
else:
    print(f"'else' block with access to char = {char}")
print("'for' loop ended\n")

# We can use for in the classic counter style using the range() function
# Python range() Function
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.
# Syntax
# range(stop) #from 0 to stop
# range(start, stop, step)
# Parameter	Description
# start	    Optional. An integer number specifying at which position to start. Default is 0
# stop	    Required. An integer number specifying at which position to stop (not included).
# step	    Optional. An integer number specifying the incrementation. Default is 1

# Range 'for' example
print("Range 'for' example")
for i in range(10): #from 0 to 9
    print(f"'for' iterator = {i}")
print("Range 'for' example ended\n")

print("Range from 4 to 10 'for' example")
for i in range(4, 10): #from 4 to 9
    print(f"'for' iterator = {i}")
print("Range from 4 to 10 'for' example ended\n")

print("Range from 2 to 10 with step 2 'for' example")
for i in range(2, 11, 2): #from 2 to 10 with step 2
    print(f"'for' iterator = {i}")
print("Range from 2 to 10 with step 2 'for' example ended\n\n")

# Loop in loop
# Example
i = 1
j = 1
print("Loop in loop")
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
print("Loop in loop ended\n\n")

# Exit from the loop. break and continue
# To control the loop, we can use the special break and continue statements. 
# The break statement exits the loop. 
# And the continue operator moves to the next iteration of the loop 
# and continues the instructions that follow it.

# break example
number = 0
print("break example")
while number < 5:
    number += 1
    if number == 3 :    # if number = 3, exit the loop
        break
    print(f"number = {number}")
print("break example ended\n\n")

# continue example
number = 0
print("continue example")
while number < 5:
    number += 1
    if number == 3 :    # if number = 3, go to a new iteration of the loop
        print(f"continue on: {number}")
        continue
    print(f"number = {number}")
print("continue example ended\n\n")