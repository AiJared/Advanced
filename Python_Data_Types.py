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