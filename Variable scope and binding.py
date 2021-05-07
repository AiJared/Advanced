def counter():
    num = 0
    def incrementer ():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter ()
print(c)
print(c())

# Global Variables
x = 'Hi'

def read_x():
    print(x)
print(read_x())

def read_y():
    y = 'Hey'
    print(y)
print(read_y())

x = 'Hi'
def change_local_x():
    x = 'Bye'
    print(x)
change_local_x()
print(x)

x = 'Hi'
def change_global_x():
    global x
    x = 'Bye'
    print(x)
change_global_x() # prints Bye
print(x)