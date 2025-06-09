# Kagglw Day 1

import math


print("Hello, World!")

# Aerithmetic and variables 
print(((1+3)*(2-1)/4)**6)

My_var = 1+5
print (My_var)

# Multiple variables
No_of_years = 10
Days_in_a_year = 365
Hours_in_a_day = 24
minures_in_an_hour = 60
seconds_in_a_miute = 60


# Calculate total seconds in a given number of years
Total_time = No_of_years * Days_in_a_year * Hours_in_a_day * minures_in_an_hour * seconds_in_a_miute
print(Total_time)

## FUNCTIONS
# Define function
def add_three(input_var):
    output_var = input_var + 3
    return output_var
# Call function
new_number = add_three(5)
print(new_number)

# Complex function
def payment(num_of_hours):
    pay_pretax = num_of_hours * 15
    pay_posttax = pay_pretax * (1- 0.2)
    return pay_posttax

# Call complex function
pay = payment(10)
print(pay)

# Function with multiple parameters
def payment_with_variable_inputs(num_of_hours, pay_rate, tax_rate):
    pay_pretax2 = num_of_hours * pay_rate
    pay_posttax2 = pay_pretax2 * (1-tax_rate)
    return pay_posttax2
# Call function with multiple parameters
pay2 = (payment_with_variable_inputs(20, 24, 0.8))
print(pay2)


# Exercise: House cost calculator
def get_expected_cost(beds, baths):
    value = 80000 +((30000*beds)+(10000*baths))
    return value
House_value = get_expected_cost(3, 2)
print(House_value)

# call the function with different parameters
# Using the get_expected_cost function to fill in each value
option_one = get_expected_cost(2,3)
option_two = get_expected_cost(3,2)
option_three = get_expected_cost(3,3)
option_four = get_expected_cost(3,4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Exercise: Function to calculate the cost of paint
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = (((sqft_walls + sqft_ceiling)/sqft_per_gallon) * cost_per_gallon)
    return cost
# Call the function with example values
cost_of_paint = get_cost(1000, 500, 400, 25)
print(cost_of_paint)

# use of math.ceil to round up the gallons of paint needed
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = (sqft_walls + sqft_ceiling)
    gallon_required = (total_sqft/sqft_per_gallon)
    gallons_to_buy = math.ceil(gallon_required)
    cost = (gallons_to_buy * cost_per_gallon)
    return cost
cost_of_paint = get_actual_cost(1000, 500, 400, 25)
print(cost_of_paint)

## DATA TYPES
almost_pi = 22/ 7
print(almost_pi)
# Data type conversion
pi = float(almost_pi)
print(pi)
# Check data type
print(type(pi))
# Round pi to 5 decimal places
pi_rounded = round(pi, 5)
print(pi_rounded)
# Check data type after rounding
print(type(pi_rounded))

# Boolean data type
# has 1 of 2 values: True or False
z_one = True
z_two = False
# Check data type of boolean
print(type(z_one))
print(type(z_two))
# Boolean operations
z_three = (1< 2)
print(z_three)
print(type(z_three))
# Boolean operations with strings using not
z_three = not z_two
print(z_three)

# String data type
w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))  # Length of the string

shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))  # Length of the empty string

# Number inside of a quotation becomes a string
number_string = "123.45"
print(type(number_string))
print(len(number_string))  # Length of the string representation of a number

Also_my_string = float(number_string) # Designationg a variable as a float
print(type(Also_my_string))  # Convert string to float
print(len(str(Also_my_string)))  # Length of the string representation of the float

# String Addition
new_string = "abc" + "def"
print(new_string)  # Concatenation of strings
print(type(new_string))  # Check data type of the new string
# String Multiplication
multiplied_string = "abc" * 3 ## cant multiply a string by a float
print(multiplied_string)  # Repeats the string 3 times
print(type(multiplied_string))  # Check data type of the multiplied string
