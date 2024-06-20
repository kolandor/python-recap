# Conditional constructs use conditional expressions and, 
# depending on their meaning, direct program execution along one of the paths. 
# One such construct is the if construct. It has the following formal definition

# Structure
# if boolean expression: 
#     instructions
# [elif boolean expression: 
#     instructions]
# [else: 
#     instructions]

# Example
x = 10
if x == 10 :
    print("It's True")
else:
    print("It False")

# else block
# If suddenly we need to define an alternative solution 
# in case the if expression returns False, then we can use the else block

# Since in Python, null and empty data types are considered False (and, conversely, non-null and non-empty True),
# then the conditional operator If can also accept, as a parameter, not only a result in the form of a Boolian.
# For example, in this case we pass the integer number 0 to the conditional operator (it is identical to False)
x = 0
if x :
    print("It's True")
else:
    print("It's False")

# elif block
# If it is necessary to introduce several alternative conditions, 
# then additional elif blocks can be used, followed by a block of instructions.
language = "german"
if language == "english":
    print("Hello")
elif language == "german":
    print("Hallo")
elif language == "french":
    print("Salut")
else:
    print("Привет")

# Nested if constructs
# The if construct, in turn, can itself have nested if constructs
language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")