#  Bitwise NOT
~0
~1
~2
~123
#  When applied to negative numbers
~-0
~-1
~-2
~-123

# Bitwise XOR(Exclusive OR)
60 ^ 30
bin(60 ^ 30)

#  Bitwise AND
60 & 30
bin(60 & 30)

#  Bitwise OR
60 | 30
bin(60 | 30)

#  Bitwise Left Shift
2 << 2
bin(2 << 2)
# Performing a left bit shift of 1 is equivalent to multiplication by 2
7 << 1
3 << 4

#  Bitwise Right Shift
8 >> 2
bin(8 >> 2)

# Performing a right bit shift of 1 is equivalent to integer division by 2
36 >> 1
15 >> 1

48 >> 4
59 >> 3

#  Inplace Operations
a = 0b001
a &= 0b010
a = 0b001
a |= 0b010
a = 0b001
a <<= 2
a = 0b100
a >>= 2
a = 0b101
a ^= 0b011