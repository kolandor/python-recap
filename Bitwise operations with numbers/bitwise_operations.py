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
print(f"Basic using interpolated string {number:0b}")

# # use the alternative form (adds the 0b prefix)
# 0 pad with zeros
# 10 pad to a total length off 10 (this includes the 2 chars for 0b)
# b use binary representation for the number
print(f"Basic with # {number:#010b}")

#Using format with prefix
print("Format using with prefix:", format(number, "#010b"))
# # use the alternative form (adds the 0b prefix)
# 0 pad with zeros
# 10 pad to a total length off 10 (this includes the 2 chars for 0b)
# b use binary representation for the number

#Using format without prefix
print("Format using without prefix:", format(number, "010b"))


print("Inline format using: {:#010b} use format specifier".format(number))

print("Using bin() function with zfill(8) to fill left side of number with zeros:", bin(number)[2:].zfill(8))

#Binary operations
#Binary AND
bx = 0b101
by = 0b110
bz = bx & by
# to output I use the interpolated multilines string
result = f'''
Binary AND
&{bx:08b}
 {by:08b}
 --------
 {bz:08b}
'''
print(result)

#Binary OR
bx = 0b101
by = 0b110
bz = bx | by
# to output I use the interpolated multilines string
result = f'''
Binary OR
|{bx:08b}
 {by:08b}
 --------
 {bz:08b}
'''
print(result)

#Invert number
bx = 0b101
bz = ~bx
# to output I use the interpolated multilines string
result = f'''
Invert number
~{bx}
--
{bz}
Same as: result = -({bx}+1) or -{bx} - 1
'''
print(result)

#Binary shift left
bx = 0b101
shift = 2
bz = bx << shift
# to output I use the interpolated multilines string
result = f'''
Binary shift left
{bx:08b} << {shift} = {bz:08b}
'''
print(result)

#Binary shift right
bx = 0b10100000
shift = 2
bz = bx >> shift
# to output I use the interpolated multilines string
result = f'''
Binary shift right
{bx:08b} >> {shift} = {bz:08b}
'''
print(result)