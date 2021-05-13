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