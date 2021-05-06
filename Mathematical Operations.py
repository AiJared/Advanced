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
#  Exponential
a, b = 2, 3
(a ** b)
pow(a, b)

import math
math.pow(a,b)

import operator
operator.pow(a, b)

a, b, c = 2, 3, 2
pow(a, b, c)

#  Special Functions
import math
import cmath
c = 4
math.sqrt(c)
cmath.sqrt(c)

import math
x = 8
math.pow(x, 1/3)
#  The function math.exp(x) computes e ** x
math.exp(0)
math.exp(1)
#  The function math.expm1(x) computes e ** x - 1
math.exp(x) - 1

math.expm1(0)

math.exp(1e-6) - 1
math.expm1(1e-6)

# Trigonometric Functions
a, b = 1, 2
import math
math.sin(a)
math.cosh(b)
math.atan(math.pi)
math.hypot(a, b)
#  Calculating Euclidian Distance between two points using math.hypot()
math.hypot(x2-x1, y2-y1)
math.degree(a)
math.radians(57.29577951308232)

#  Inplace Operations
a = a + 1
a = a * 2
a += 1
a *= 2