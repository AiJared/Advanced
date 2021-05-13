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