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