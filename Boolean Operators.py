#  'and', 'or' are not guaranteed to retrun a boolean
def or_(a, b):
    if a:
        return a
    else:
        return b

def and_(a, b):
    if not a:
        return a
    else:
        return b

if 3.14 < x < 3.142:
    print('x is near pi')

#  Short circuit Evaluation
def true_func():
    print("true_func()")
    return True

def false_func():
    print("false_func()")
    return False
true_func() or false_func()
false_func() or true_func()
true_func() and false_func()
false_func() and false_func()

# And
x = True
y = True
z = x and y
x = True
y = False
z = x and y
x = False
y = True
z = x and y
x = False
y = False
z = x and y
x = 1
y = 1
z = x and y
x = 0
y = 1
z = x and y
x = 1
y = 0
z = x and y
x = 0
y = 0
z = x and y

# OR
x = True
y = True
z = x or y
x = True
y = False
z = x or y
x = False
y = True
z = x or y
x = False
y = False
z = x or y
x = 1
y = 1
z = x or y
x = 1
y = 0
z = x or y
x = 0
y = 1
z = x or y
x = 0
y = 0
z = x or y
# NOT
x = True
y = not x

x = False
y = not x