"""
Variables are designed to store data. 
A variable name in Python must begin with an alphabetic character 
or an underscore and can contain alphanumeric characters and an underscore. 
And besides, the name of the variable should not coincide with the name of the Python language keywords. 
There are not many keywords, they are easy to remember:

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""

#Cases example
helloPhrase = "Hello, "
name = "Alex"
end_sign = "!"
print(helloPhrase + name + end_sign)

#Modifying variable data
name = "Nina"
print(helloPhrase + name + end_sign)

#Bool variables
isConnected = True
print("Is internet connected:", isConnected)

#Integer variables
myAge = 31
print("My age is: ", myAge)

#BIN integer variables
bin = 0b1011 #is 11 integer
print("Binary 1011 =", bin)

#OCT integer variables
oct = 0o10 #is 8 integer
print("Oct 10 =", oct)

#HEX integer variables
hex = 0xFF #is 255 integer
print("Hex FF =", hex)

#Float variables
circumference = 10
diameter = 3.18
Pi = circumference / diameter
print("π = circumference / diameter =", Pi)

#Also you can asign float like that
weght = 99.
print("Weight asign 99.:", weght)

#Scientific notation
x = 3.9e3
print("Scientific notation 3.9e3 =", x)  # 3900.0
x = 3.9e-3
print("Scientific notation 3.9e-3 =", x)  # 0.0039

#Strings
#Regular strings
text = 'Hello'
text = "World"

#In Python, there is no significant difference between 
#using single quotes (') and double quotes ("") to define strings.

#String contains double quotes
text = 'Hello "World"!'
#Same as
text = "Hello \"World\"!"

#And vice versa
text = "Hello 'World'!"
#Same as
text = 'Hello \'World\'!'

#Multiline string
text = """This
Is
Multiline
String
"""
#Also Multiline string
text = '''This
Is
Multiline
String
'''

#Lines with xscape sequences
text = '''
\\: allows you to add a slash inside a string

\': allows you to add a single quote inside a string

\": allows you to add a double quote inside a string

\n: breaks to a new line

\t: adds tab (4 indents)
'''

#Lines withOUT xscape sequences
text = r'Hello \n World'

#Interpolated strings with the ability to insert values ​​and perform operations directly in the string
text = f"Hello {name}!"
print(text)
text = f"5 + 5 = {5 + 5}"
print(text)

#Dynamic typing
anyType = "Hello!"
#Using the built-in type() function, you can dynamically find out the current type of a variable
print(f"{anyType} : Type is: {type(anyType)}")

anyType = True
print(f"{anyType} : Type is: {type(anyType)}")
anyType = 10
print(f"{anyType} : Type is: {type(anyType)}")
anyType = 3.14
print(f"{anyType} : Type is: {type(anyType)}")