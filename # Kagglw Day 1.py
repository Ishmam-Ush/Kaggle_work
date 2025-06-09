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