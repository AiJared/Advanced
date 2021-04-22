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
# List Data Types
list = [123, 'abcd', 10.2, 'd']  #can be an array of any data type or single dta type
list1 = ['Hello', 'world']
print(list)  # will output the whole list
print(list[0:2])  # will output first two elements of the list
print(list1 * 2)  # will give list1 two times
print(list + list1)  # will give concatenation of both lists
# Dictionary Data Types
dic={'name': 'red', 'age': 10}
print(dic)  # will output the key-value pairs
print(dic['name'])  # will output only value with 'name' key
print(dic.values())  # will output the list of values in dic
print(dic.keys())  # will output the list keys