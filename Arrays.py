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
my_array.insert(0,0)
print(my_array)
#  Extend Array using extend() method
my_extnd_array = array('i', [7, 8, 8, 10])
my_array.extend(my_extnd_array)
print(my_array)
#  Add items from list into array using fromlist() method
c = [11, 12, 13]
my_array.fromlist(c)
print(my_array)
#  Remove any array element using remove() method
my_array.remove(4)
print(my_array)
#  Remove last element using pop() method
my_array.pop()
print(my_array)
#  Fetch any element through its index using index() method
print(my_array.index(5))
print(my_array.index(3))
