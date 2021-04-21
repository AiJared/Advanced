# Creating Variables and Assigning Values
a = 2
print(type(a))
pi = 3.14
print(type(pi))
c = 'A'
print(type(c))
name = 'John Doe'
print(type(name))
q = True
print(type(q))
x = None
print(type(x))
a, b, c = 1, 2, 3
print(a, b, c)
a = b = c = 1 # All three objects refer to one int object 1
print(a, b, c)
b = 2          # b now refers to another int object, one with a value 1
print(a, b, c)
# The Same could Apply to mutable types (list, dict etc)
x = y = [7, 8, 9]   # x and y refer to same list object just created[7, 8, 9]
x = [13, 8, 9]      # x now refers to a different list object just created[13, 8, 9]
print(x, y)
x = y = [7, 8, 9]   # x and y are two different names for the same list object just created[7, 8, 9]
x[0] = 13           # we are updating the value of the list [7, 8, 9] through one of its names x in this case
print(y)            # printing the value of the list using its other name
print(x)
# Nested Lists are also valid. This means that a list can also contain another list as an element
x = [1, 2, [3, 4, 5], 6, 7] # this is a nested list
print(x[2])
print(x[2][1])
# You can assign a new value to a variable using (=)
a = 2
print(a)
a = "Jared"
print(a)
# Block Indentation
def my_function():  # This is the function definition. Note the colon(:)
    a = 2           # This line belongs to the function because it is indented
    return a        # This line also belongs to the same function
print(my_function)  # This line is outside the function block
i = 10
k = 20
if i < k:
    print(i)
else:
    print(k)
# Data Types
# Booleans
issubclass(bool, int)
isinstance(True, bool)
isinstance(False, bool)
True + False == 1
True * True == 1
# Integers
a = 2
b = 10
# Floats
c = 2.0
d = 100.e0
e = 123456789.e1
# Complex Numbers
i = 2 + 1j
k = 100 + 10j
# Sequences and Collections
# List
a = [1, 2, 3, 4]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else'
# set
a = {1, 2, 'a'}
# Dictionary
a = {1: 'one',
     2: 'two'}

b = {'a': [1, 2, 3],
     'b': 'a string'}
# Using Conditional Statements to test for Data types
i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1
# Converting between Data types
a = '123'
b = int(a)
a = '123.456'
b = float(a)
d = int(b)
# You can also convert sequence or collections types
a = 'hello'
list(a)
set(a)
tuple(a)
# Mutable and Immutable Data Types
def f(m):
    m.append(3)  # adds a number to the list. This is a mutation
x = [1, 2]
f(x)
# Immutable
def bar():
    x = (1, 2)
    g(x)
    x == (1, 2) # Will always be True, since no function can change the object (1, 2)
# Collection Types
# Lists
int_list = [1, 2, 3]
string_list = ['Jared', 'Otieno']
print(int_list, string_list)
empty_list = [] # empty list
mixed_list = [10, 'Mercy', True, 5.75, None]
print(mixed_list)
# Accessing the Elements pf a list via an index
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])
print(names[-5])
# Lists are mutable, you change the values in a list
names[0] = 'Ann'
print(names)
# Adding/removing elements in a list
names.append("Sia")
print(names)
# Add a new element at a specific index
names.insert(1, "Nikki")
print(names)
names.insert(3, "Ayuma")
print(names)
names.remove("Bob")
print(names)
# Getting the index of an Element in a list
names.index("Ann")
print(names.index("Ann"))
# Count length of lists
len(names)
print(len(names))
# Count occurence of any item in the list
a = [1, 1, 1, 2, 3, 4]
a.count(1)
print(a.count(1))
# Reverse the list
a.reverse()
print(a)
a[::-1]
print(a)
# Remove and return item at index
names.pop(1)
print(names.pop(1))
# You can iterate over the list elements like below
def my_list():
    for element in my_list:
        print(element)
# Tuples
ip_address = ('10.20.30.40', 8080)
print(ip_address)
one_member_tuple = ('Only member')
one_member_tuple = 'Only member'
one_member_tuple = tuple(['Only member'])
print(one_member_tuple)
# Dictionaries
state_capitals = {
    'Arkansas': 'Little Rock',
     'Colorado': 'Denver',
     'California': 'Sacramento',
     'Georgia:': 'Atlanta'
}
# To get a value refer to it by key
ca_capital = state_capitals['California']
print(ca_capital)
for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))
# Set
first_names = {'Adam', 'Beth', 'Charlie'}
print(first_names)
my_list = [1, 2, 3]
my_set = set(my_list)
print(my_set)
# Check Membership of the set using in:
if name in first_names:
    print(name)
# Defaultdict
state_capitals = {
    'Arkansaa': 'Little Rock',
     'Colorado': 'Denver',
     'California': 'Sacramento',
     'Georgia:': 'Atlanta'
}
from collections import defaultdict
state_capitals = defaultdict(lambda: 'Boston')
state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'
state_capitals['Colorado'] = 'Denver'
state_capitals['Georgia'] = 'Atlanta'
state_capitals['Alabama']
print(state_capitals['Alabama'])
print(state_capitals['Arkansas'])
# User Input
# Interactive Input
name = input("What is your name?")
print(name)
x = input("Write a number:")
float(x) / 2
# Built in Modules and Functions
import math
math.sqrt(16)
print(math.sqrt(16))