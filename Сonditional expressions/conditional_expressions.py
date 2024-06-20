# A number of operations represent conditional expressions.
# All of these operations take two operands and return a Boolean value,
# which in Python represents the type bool.
# There are only two logical values ​​- True (the expression is true) and False (the expression is false).

# Comparison Operations
# The simplest conditional expressions represent comparison operators that compare two values.
# Python supports the following comparison operations:
# ==
# Returns True if both operands are equal. Otherwise it returns False.
# !=
# Returns True if both operands are NOT equal. Otherwise it returns False.
# > (more than)
# Returns True if the first operand is greater than the second.
# < (less than)
# Returns True if the first operand is less than the second.
# >= (greater than or equal to)
# Returns True if the first operand is greater than or equal to the second.
# <= (less than or equal to)
# Returns True if the first operand is less than or equal to the second.

# These are classic expressions, so I won't go into them in detail.
# It is worth understanding that since Python is a scripting programming 
# language with non-strict data types, it will compare any data types with each other, 
# but without type casting, so the answer will be False
number = 10
string = "10"
print("number == string", number == string) #False
print("string == number", string == number) #False
print("string == str(number)", string == str(number)) #True
print("int(string) == number", int(string) == number) #True

# False and True
# Everything in Python that is not 0 and not empty is considered true.
string = ""
print('string = ""', bool(string))
number = 0
print('number = 0', bool(number))
string = "hello"
print('string = "hello"', bool(string))
number = 10
print('number = 10', bool(number))

# Logical Union Operations

# The "and" operator applies to two operands:
# x and y
# The and operator first evaluates the expression x, 
# and if it is False, then its value is returned. If it is True, 
# then the second operand, y, is evaluated and the value of y is returned.
# It turns out that if x is True then, regardless of whether it is, 
# the operator returns the right value
x = True
y = 10
print("x(True) and y(10): ", x and y) 
x = 0
y = 10
print("x(0) and y(10): ", x and y) 

# The and operator and other combining operators work with all types of data, 
# they work with them as Boolean, but returning 
# a value does not convert them to a boolean

age = 22
weight = 58
result = age > 21 and weight == 58
print("result = age > 21 and weight == 58:",result)  # True

# The "or" operator
# The or operator first evaluates the expression x, 
# and if it is True, then its value is returned. 
# If it is False, then the second operand, y, is evaluated and the value of y is returned 
# (regardless of whether the second value is True or False)

x = True
y = 10
print("x(True) or y(10): ", x or y) 
x = False
y = 0
print("x(False) or y(0): ", x or y)

age = 22
isMarried = False
result = age > 21 or isMarried
print("age(22) > 21 or isMarried:", result) #True

# Python Logical Operators

# The "not" operator
# Returns True if expression is False
# Works with any types, but returns only boolean
age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True
print(not 4)  # False
print(not 0)  # True
x = 5
print(not(x > 3 and x < 10))# returns False because not is used to reverse the result

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x # same object as

# Operator "is"
# Returns True if both variables are the same object

print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Operator "is not"
# Returns True if both variables are not the same object

print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object

# Operator in
# Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = "Hello world!"
y = "world"
print(f"Check '{y}' in '{x}':", y in x)

# Operator not in
# Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

x = "Hello world!"
y = "world"
print(f"Check '{y}' not in '{x}':", y not in x)
y = "cake"
print(f"Check '{y}' not in '{x}':", y not in x)