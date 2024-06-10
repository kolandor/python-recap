#Classic operations
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)

#Integer division of two numbers:
print("5 // 2 =", 5 // 2) #Trimming the remainder after the decimal point (not rounding)

#Raising a number to a power:
print("5 ** 2 =", 5 ** 2)

#Getting the remainder of a division:
print("5 % 2 =", 5 % 2)

# When several arithmetic operations are used sequentially, 
#they are executed in accordance with their priority. 
#Operations with higher priority are performed first. 
#The priorities of operations in descending order are shown in the following table.

# Operations Direction

# **        Right to left

# * / // %  From left to right

# + -       From left to right

# It should be noted that arithmetic operations 
# can involve both whole and fractional numbers. 
# If an integer (int) and a floating-point number (float) 
# are involved in the same operation, then the integer is cast to the float type.

# Arithmetic operations with assignment
# A number of special operations allow you to 
# use the assignment of the result of an operation to the first operand:

number = 5
print(f"number is: {number}")
number += 2
print(f"number += 2\nnumber is: {number}")
number -= 2
print(f"number -= 2\nnumber is: {number}")
number *= 2
print(f"number *= 2\nnumber is: {number}")
number /= 2
print(f"number /= 2\nnumber is: {number}")
number //= 2
print(f"number //= 2\nnumber is: {number}")
number **= 2
print(f"number **= 2\nnumber is: {number}")
number %= 2
print(f"number %= 2\nnumber is: {number}")

#Real math round
# The round() function returns a floating point number that is a rounded version of the specified number, 
# with the specified number of decimals.

# The default number of decimals is 0, meaning that the function will return the nearest integer.

#Syntax
#round(number, digits)
# Parameter	    Description
# number	    Required. The number to be rounded
# digits	    Optional. The number of decimals to use when rounding the number. Default is 0

#Example
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(f"{first_number} + {second_number} = {third_number}")
print(f"Rounded by default: {round(third_number)}")  # 2

print(f"Rounded by 4 sign: {round(third_number, 4)}")  # 2.1001

#Math round example
print(f"Math round: 2.49 = {round(2.49)}")  # 2
print(f"Math round: 2.51 = {round(2.51)}")  # 3

#!!!!!!!!!!!ATTENTION NOT EXPECTED
# However, if the part being rounded is equally distant from two integers, 
#then rounding goes to the nearest even number:

print(f"Python \"math\" round: 2.5 = {round(2.5)}")   # 2 - nearest even
print(f"Python \"math\" round: 3.5 = {round(3.5)}")   # 4 - nearest even

# Rounding is done to the nearest multiple of 10 to the power minus the part being rounded:
print(f"Round nearest multiple of 10: 2.499 = {round(2.499, 2)}")    # 2.5

#!!!!!!!!!!!ATTENTION NOT EXPECTED
#answers can be there:
#https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues
#but thats dangeruos situation
print("Round 2.5549 to 3 digit =", round(2.5549, 3))
print("Round 2.5549 to 3 digit and than to 2 =", round(round(2.5549, 3), 2))
print("Round 2.5549 to 2 digit =", round(2.5549, 2))

# In Python, due to the fact that the decimal part of a number 
# cannot be accurately represented as a float number, this can 
# lead to some unexpected results. 
# For example:


print("Round 2.545 to 2 digit, Expected 2.54, Result =", round(2.545, 2))   # 2.54
print("Round 2.555 to 2 digit, Expected 2.56, Result =", round(2.555, 2))   # 2.56
print("Round 2.565 to 2 digit, Expected 2.56, Result =", round(2.565, 2))   # 2.56
print("Round 2.575 to 2 digit, Expected 2.58, Result =", round(2.575, 2))   # 2.58
 
print("Round 2.655 to 2 digit, Expected 2.66, Result =", round(2.655, 2))   # 2.65
print("Round 2.665 to 2 digit, Expected 2.66, Result =", round(2.665, 2))   # 2.67
print("Round 2.675 to 2 digit, Expected 2.68, Result =", round(2.675, 2))   # 2.67

# One illusion may beget another. For example, since 0.1 is not exactly 1/10, 
# summing three values of 0.1 may not yield exactly 0.3, either:
print("0.1 + 0.1 + 0.1 == 0.3 Result:", 0.1 + 0.1 + 0.1 == 0.3)

# Also, since the 0.1 cannot get any closer to the exact value of 1/10 and 0.3 
# cannot get any closer to the exact value of 3/10, then pre-rounding with round() function cannot help:
print("round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1) Result:", round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))

#SOLUTION!!!
# Though the numbers cannot be made closer to their intended exact values, 
# the math.isclose() function can be useful for comparing inexact values:
import math
print("math.isclose(0.1 + 0.1 + 0.1, 0.3) Result:", math.isclose(0.1 + 0.1 + 0.1, 0.3))
#More about ROUND problems here: https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues