# Kagglw Day 1

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

