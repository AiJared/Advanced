#  Access Individual elements through indexes
from array import *
my_array = array('i', [1, 2, 3, 4, 5])
print(my_array[1])
print(my_array[2])
print(my_array[0])
for i in my_array:
    print(i)
#  Append any value to the array using append() method
my_array.append(6)
print(my_array)