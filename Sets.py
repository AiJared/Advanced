#  Operation on Sets
# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6} # {3, 4, 5}
# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6} # {1, 2, 3, 4, 5, 6}
# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
{1, 2, 3, 4} - {2, 3, 5} # {1, 4}
# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}
# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
{1, 2} >= {1, 2, 3} # False
# Subset check
{1, 2}.issubset({1, 2, 3}) # True
{1, 2} <= {1, 2, 3} # True
# Disjoint check
{1, 2}.isdisjoint({3, 4}) # True
{1, 2}.isdisjoint({1, 4}) # False

#  With single elements
2 in {1, 2, 3}
4 in {1, 2, 3}
4 not in {1, 2, 3}

# Add and remove
s = {1, 2, 3}
s.add(4)

s.discard(3)
s.remove(2)
s = {1, 2}

s.upadate({3, 4})

#  Get the unique elements of a list
restaurants = ["McDonald's", "Buger king", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)

list(unique_restaurants)
list(set(restaurants))

#  Sets of sets
{frozenset({1, 2}), frozenset({3, 4})}

#  Set opearations using methods and Builtins
a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}
a.intersection(b)
a.union(b)
a.difference(b)
b.difference(a)
a.symmetric_difference(b)
b.symmetric_difference(a)
c = {1, 2}
c.issubset(a)
a.issuperset(a)
d = {5, 6}
a.isdisjoint(d)
len(a & d) == 0
a & d == set()
1 in a
len(a)
len(b)

#  Sets versus multisets
setA = {'a', 'b', 'b', 'c'}
listA = ['a', 'b', 'b', 'c']
from collections import Counter
counterA = Counter(['a','b','b','c'])
counterA

#  Mathematical Operations
# Python Division
a, b, c, d, e = 3, 2, 2.0 -3, 10
a / b # = 1
a / c # = 1.5
d / b # = -2
b / a # = 0
d / e

# You can also use operator module
import operator
operator.div(a, b)
operator.__div__(a, b)

#  float division
from __future__ import division
a / b
a // b

a / (b * 1.0)
1.0 * a / b
a / b * 1.0
from operator import truediv
truediv(a, b)
a / b
e / b
a // b
a // c
import operator # the operator module provides 2-argument arithmetic functions
operator.truediv(a, b)
operator.floordiv(a, b)
operator.floordiv(a, c)

#  Addition
a, b = 1, 2
a + b
a +=b
import operator
operator.add(a, b)
a = operator.iadd(a, b)