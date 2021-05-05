from enum import Enum
class color (Enum):
    red = 1
    green = 2
    blue = 3

print(color.red)
print(color(1))
print(color['red'])
print(color(2))
print(color['blue'])

#  Iteration
#  Enums are iterable
class color(Enum):
    red = 1
    green = 2
    blue = 3

[c for c in color]