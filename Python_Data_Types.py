# String Data Type
a_str = "Hello World"
print(a_str)  # Output will be whole string
print(a_str[0])  # Output will be first character H
print(a_str[0:5])  # Output will be the first five characters. Hello
Name = "Jared"
print(Name)
print(Name[0:2])
Names = ("Mercy", "Sure", "Abby", "Karen", "Hellen", "Grace", "Lydia")
print(Names)
print(Names[0:2])
# Set Data Types
# They are mutable and new elements can be added once sets are defined
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # duplicate will be removed
a = set('abracadabra')
print(a)  # unique letters in a
a.add('z')
print(a)
# Frozen Sets
# They immutable and new elements cannot be added after its defined
b = frozenset('asdfagsa')
print(b)
cities = frozenset(["Frankfurt", "Basel", "Freiburg"])
print(cities)
# Numbers Data type
int_num = 10 # int value
float_num = 10.2  # float value
complex_num = 3.14j  # complex value
long_num = 1234567  # Long value
print(int_num)
print(float_num)
print(complex_num)
print(long_num)