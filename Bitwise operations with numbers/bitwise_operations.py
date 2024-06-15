#Bitwise operations with numbers

#To output a decimal number in binary, you can use the 0b specifier:
number = 5 #binary 101
print(f"DEC {number} = BIN {number:0b}")

#Python allows you to immediately define a number in binary form.
# To do this, the number in binary form is indicated after the prefix 0b:
number = 0b101 #Binary determination
print(f"DEC {number} = BIN {number:0b}")

#Binary format strings
#There are many ways to display a number in binary notation.
number = 4
#Basic way
print(f"Ways to display a number {number} in binary:")
print(f"Basic {number:0b}")

#Using format with prefix
print("Format using with prefix:", format(number, "#010b"))
# # use the alternative form (adds the 0b prefix)
# 0 pad with zeros
# 10 pad to a total length off 10 (this includes the 2 chars for 0b)
# b use binary representation for the number

#Using format without prefix
print("Format using without prefix:", format(number, "010b"))


#Binary operations
#Binary AND
# bx = 0b101
# by = 0b110
# bz = bx & by
#to output I use the interpolated multilines string
# result = f'''
# {bx:0b}
# &
# {by:0b}
# ----
# {bz:08b}
# '''
# print(result)