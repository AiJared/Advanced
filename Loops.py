#  Break and continue in Loops
#  Break Statement
i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking for loop")
        break
    i += 1
#  break Statements in for loop
for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break
# Continue Statement
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)
#  Nested Loops
while True:
    for i in range(1, 5):
        if i == 2:
            break
#  Use return from within a function as a break
def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return (i)
        print(i)
    return (5)
#  Return statement in nested loops
def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i*j == 6:
                return(i)
            print(i*j)
#  For loops
for i in (0, 1, 2, 3, 4):
    print(i)
for i in range(1, 5):
    print(i)
#  Iterating Over lists
for x in ['one', 'two', 'three', 'four']:
    print(x)
for x in range(1, 6):
    print(x)
#  Enumerate Function
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)
#  Iterate over lists value manipulation using map and lambda
x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(x)
#  Loops with an else clause
for i in range(3):
    print(i)
else:
    print('done')
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')
#  else does not execute if the loop terminates through s break or exeption
for i in range(2):
    print(i)
    if i == 1:
        break
    else:
        print('done')
# The main use case for the for...else construct is a concise implementation of search as for instance:
a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
    else:
        print('no exception')
#  The pass statement
for x in range(10):
    pass
while x == y:
    pass
#  Iterating Over Dictionaries
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print('key')
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, "::", value)
#  The 'half loop" do-while
a = 10
while True:
    a = a-1
    print(a)
    if a<7:
       break
print('Done.')
#  Iterating different portion of a list with different step size
#  Iteration over the whole list
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for s in lst:
    print (s[:1])
for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))
#  Iterate Over sub-list
for i in range(2,4):
    print("lst at %d contains %s" % (i, lst[i]))
for s in lst[1::2]:
    print(s)
for i in range(1, len(lst), 2):
    print(lst[i])