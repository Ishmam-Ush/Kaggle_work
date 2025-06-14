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

# Higher order functions

def mod_5(x):
    """
    Returns the remainder of x divided by 5."""
    return x % 5
print(
    "The largest number is",
    max(100,63,21),
    "the largest number with the largest remainder is",
    max(100, 63, 14, key=mod_5),
    sep='\n'
)

# Exercise 
def round_to_two_places(num):
    
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    
    # Replace this body with your own code.
    return round(num, 2)
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)

# Second exercise
# Put your test code here
print(round(1234.567, 2))   # rounds to 2 decimal places → 1234.57
print(round(1234.567, 0))   # rounds to whole number → 1235.0
print(round(1234.567, -1))  # rounds to nearest 10 → 1230.0
print(round(1234.567, -2))  # rounds to nearest 100 → 1200.0
print(round(1234.567, -3))  # rounds to nearest 1000 → 1000.0

# Third exercise
def to_smash(total_candies,n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends
# 4th ex
def round_to_two_places(x):
    return round(x, 2)
print(round_to_two_places(3.1416))
 # 5th ex
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = x if abs(x) <  abs(y) else y
print(smallest_abs)
# 6th ex
def y_absolute(x):
    y = abs(x)
    return y

print(y_absolute(-5))

### Booleans and conditionals

def can_run_for_president(age):
    """Return True if the person can run for president, False otherwise."""
    return age >=35
print("can a 19 year old run for president?" ,can_run_for_president(19))
print("can a 35 year old run for president?" ,can_run_for_president(35))
print("can a 40 year old run for president?" ,can_run_for_president(40))

# odd/even
def is_odd(n):
    """Return True if n is odd, False otherwise."""
    return n % 2 == 1
print("Is 3 odd?", is_odd(3))
print("Is 4 odd?", is_odd(4))