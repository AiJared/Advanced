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