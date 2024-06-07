# Console IO

#Console output
# The print() function prints the specified message to the screen, or other standard output device.

# The message can be a string, or any other object, 
# the object will be converted into a string before written to the screen.

#Syntax
#print(object(s), sep=separator, end=end, file=file, flush=flush)

# Parameter	Description
# object(s)	Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	Optional. An object with a write method. Default is sys.stdout
# flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

#Examples
print("Hello World!")
print("Hello", "World", "!", sep="_")
print("Hello", end=" my ")
print("World!")
f = open("hello.txt", "w+t")
print("Hello File!", file=f)
f.seek(0)
print("Text from file:", f.read(), end="\n\n")
f.close

#Console input
#The input() function allows user input.

# Syntax
# input(prompt)

# Parameter	Description
# prompt	A String, representing a default message before the input.

#Example
print("Input example")
name = input("input your name: ")
age = input("input your age: ")
print(f"Hello {name}, your age is {age}")