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