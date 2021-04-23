#  Simple Example
class ExampleClass:
    #  Every function belonging to a class must be indented equally
    def __init__(self):
     name = "example"

def someFunction(self, a):
    #  Notice everything belonging to a Function must be indented
    if a > 5:
        return True
    else:
        return False
#  If a function is not indented to the same level it will not be considered as part of the parent class
def separateFunction(b):
    for i in b:
        #  Loops are also indented and nested conditions start a new indentation
        if i == 1:
            return True
    return False

if foo:
    if bar:
        x = 42
else:
    print(foo)