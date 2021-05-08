#  Conditional Expression (Or "the Ternary operator")
n = 5
"Greater than 2" if n < 2 else "Smaller thatn or equal to 2"
#  Ternary operators can also be nested
n = 5
"Hello" if n > 10 else "Goodbye" if n > 5 else "Good day"

# if, elif and else
number = 5

if number > 2:
    print("Number is bigger than 2.")
elif number < 2:
    print("Number is smaller than 2.")
else:
    print("Number is 2.")

#  Boolean Logic Expressions
#  And operator
1 and 2
1 and 0
1 and "Hello World"
"" and "pancakes"

# Or operator
1 or 2
None or 1
0 or []

#  Lazy evaluation
def print_me():
    print('I am here!')
0 and print_me()

#  Testing for multiple conditions
#  Each variable need to compared separately
a = 1
b = 6
if a > 2 and b > 2:
    print('yes')
else:
    print('no')
#  Checking if a variable is one of the multiple values
#  Each comparison must be made separately
a = 1
if a == 3 or a == 4 or a == 6:
    print('yes')
else:
    print('no')
#  Using the operator is the canonical way to write this
if a in (3, 4, 6):
    print('yes')
else:
    print('no')