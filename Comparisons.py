#  Chain comparisons
1 > -1 < 2 > 0.5 < 100 != 24
#  Comparison by 'is' vs '=='
a = 'Python is fun!'
b = 'Python is fun!'
a == b # True
a is b #  False

a = [1, 2, 3, 4, 5]
b = a #  b references a
a == b #  True
a is b # False
b = a[:] #  b references a copy of a
a == b #  True
a is b #  False
#  short strings and small integers will return True when compared with is
a = 'short'
b = 'short'
c = 5
d = 5
a is b #  True
c is d #  True
#  Larger strings and longer integers will be stored separately
a = 'not so short'
b = 'not so short'
c = 1000
d = 1000
a is b #  False
c is d #  False
#  is should be used to test for none
if myvar is not None:
    pass
if myvar is None:
    pass
#  using is to test for a sentinel(a unique object)
sentinel = object()
def myfunc(var=sentinel):
    if var is sentinel:
        #  Value wasn't provided
        pass
    else:
        #  Value was provided
        pass
#  Greater than or less than
12 > 4
1 < 4
#  Strings compare lexicographically(alphabetical order)
"alpha" < "beta" #  True
"gamma" > 'beta' #  True
"gamma" < "OMEGA" #  False
"GAMMA" < "OMEGA" #  True
#  Not equal to
12 != 1 #  True
12 != '12' #  True
'12' != '12' #  False
12 == 12 #  True
12 == 1 #  False
'12' == '12' #  True
'spam' == 'spam' #  True
'12' == 12 #  False
#  Comparing objects
class foo(object):
    def __init__(self, item):
        self.my_item = item
    def __eq__(self, other):
        return self.my_item == other.my_item
a = foo(5)
b = foo(5)
a == b #  True
a != b #  False
a is b #  False