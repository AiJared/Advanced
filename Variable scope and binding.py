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

#  Functions skip class scope when looking up
# names
a = 'global'
class Fred:
   a = 'class' # class scope
   b = (a for i in range(10)) # function scope
   c = [a for i in range(10)] # function scope
   d = a # class scope
   e = lambda: a # function scope
   f = lambda a=a: a # default argument uses class scope
@staticmethod # or @classmethod, or regular instance method
def g(): # function scope
    return a
print(Fred.a) # class
print(next(Fred.b)) # global
print(Fred.c[0]) # class in Python 2, global in Python 3
print(Fred.d) # class
print(Fred.e()) # global
print(Fred.f()) # class
print(Fred.g()) # global
class A:
  a = 42
  b = list(a + i for i in range(10))

#  Local vs Global Scope
foo = 1
def func():
    bar = 2
    print(foo)
    print(bar)
foo = 1
def func():
    bar = 2
    print(globals().keys()) # prints all variable names in global scope
    print(locals().keys())
#  Name classhes
foo = 1
def func():
    foo = 2 # creates a new variable foo in local scope, global foo is not affected
    print(foo) # prints 2
# global variable foo still exists, unchanged:
    print(globals()['foo']) # prints 1
    print(locals()['foo'])
#  to modify a global variable use the keyword global
foo = 1
def func():
    global foo
    foo = 2
foo = 1
def func():
# In this function, foo is a global variable from the beginning
    foo = 7 # global foo is modified
    print(foo) # 7
    print(globals()['foo']) # 7
    global foo # this could be anywhere within the function
    print(foo)
#  Functions within Functions
foo = 1
def f1():
    bar = 1
def f2():
    baz = 2
# here, foo is a global variable, baz is a local variable
# bar is not in either scope
    print(locals().keys()) # ['baz']
    print('bar' in locals()) # False
    print('bar' in globals()) # False
def f3():
    baz = 3
    print(bar) # bar from f1 is referenced so it enters local scope of f3 (closure)
    print(locals().keys()) # ['bar', 'baz']
    print('bar' in locals()) # True
    print('bar' in globals()) # False
def f4():
    bar = 4 # a new local bar which hides bar from local scope of f1
    baz = 4
    print(bar)
    print(locals().keys()) # ['bar', 'baz']
    print('bar' in locals()) # TrueGoalKicker.com – Python® Notes for Professionals 79
    print('bar' in globals()) # False
#  Global vs nonlocal
def f1():
    foo = 1
    def f2():
       foo = 2 # a new foo local in f2
       def f3():
           foo = 3 # a new foo local in f3
           print(foo) # 3
           foo = 30 # modifies local foo in f3 only
       def f4():
           global foo
           print(foo) # 0
           foo = 100 # modifies global foo

def f1():

    def f2():
        foo = 2 # a new foo local in f2

        def f3():
            nonlocal foo # foo from f2, which is the nearest enclosing scope
            print(foo) # 2
            foo = 20
#  Binding Occurrence
x = 5
x += 7
for x in iterable: pass