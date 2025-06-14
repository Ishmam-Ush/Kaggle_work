# Python code to demonstrate the use of the round function
# The round function is used to round a floating-point number to a specified number of decimal places.
help(round)  # Display help for the round function
round(3.141652654, ndigits=2)  # Rounding to 2 decimal places
round(3.141652654, ndigits=4)  # Rounding to 4 decimal places
round(3.141652654, ndigits=None)  # Rounding to 0 decimal places

# Arguments woth default values
def greet(who = "Collin"):
    print("Hello,", who)

greet()
greet(who="world")
greet("world")

# Function within a function
def mult_by_five(x):
    return 5 * x
def call(fn,arg):
    """
    Calls the function fn with the argument arg."""
    return fn(arg)
def squared_call(fn, arg):
    """
    Calls the function fn with the argument arg and returns the square of the result."""
    return fn(fn(arg))
print(
    call(mult_by_five, 5),
    squared_call(mult_by_five, 5),
    sep='\n'
)  # \n is the newline character, used to print each result on a new line