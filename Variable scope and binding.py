def counter():
    num = 0
    def incrementer ():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter ()
print(c)
print(c())

# Global Variables
x = 'Hi'

def read_x():
    print(x)
print(read_x())

def read_y():
    y = 'Hey'
    print(y)
print(read_y())

x = 'Hi'
def change_local_x():
    x = 'Bye'
    print(x)
change_local_x()
print(x)

x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
change_global_x() # prints Bye
print(x)

#  Local Variables
def foo():
    a = 5
    print(a)

def foo():
    if True:
     a = 5
     print(a)

#  The del command
x = 5
print(x) # out: 5
del x
class A:
    pass
a = A()
a.x = 7
print(a.x) # out: 7
del a.x
x = {'a': 1, 'b': 2}
del x['a']
print(x)
x = [0, 1, 2, 3, 4]
del x[1:3]
print(x) 