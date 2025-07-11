# Kaggle Day 2

# If statement (Fever exp)
def evaluate(temp):
    message = "normal temperature"
    if temp > 40:
        message = "High fever"
        return message
print(evaluate(41))  # High fever

# if else statement
def evaluate_temp(temp):
    if temp >40:
        return "High fever"
    else:
        return "Normal temperature"
print(evaluate_temp(39))  # Normal temperature

# if elif else statement
def evaluate_temperature(temp):
    if temp > 40:
        return "High fever"
    elif temp > 37:
        return "Low fever"
    else:
        return "Noermal temperature"
print(evaluate_temperature(39)) # Low fever

# Tax calculation

def earnings(pay):
    if pay >= 12000:
        tax = 0.30*pay
    elif pay < 12000:
        tax = 0.25 *pay
    return tax 
print(earnings(15000))  # 4500.0
print(earnings(10000))  # 2500.0

# grade calculation
def get_grade(score):
    grade = "A","B","C","D","F"
    if score >= 90: 
        return  "A"
    elif score >= 80:
        return  "B"
    elif score >= 70:
        return  "C"
    elif score >= 60:
        return  "D"
    elif score < 60:
        return  "F"
print(get_grade(95))  # A
print(get_grade(85))  # B
print(get_grade(75))  # C
print(get_grade(65))  # D
print(get_grade(55))  # F


# Gold plate calculation
def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10*len(engraving)
    else:
        cost = 50 + 7*len(engraving)
    return cost
print(cost_of_project("Happy Birthday", True))  # 170
print(cost_of_project("Happy Birthday", False))  # 119


# Water bill calculation
def get_water_bill(num_gallons):
    bill = 1000
    if num_gallons <= 8000:
        bill = (num_gallons/1000)*5
    elif num_gallons <= 22000:
        bill = (num_gallons/1000)*6
    elif num_gallons <= 30000:
        bill = (num_gallons/1000)*7
    elif num_gallons >= 30000:
        bill = (num_gallons/1000)*10
    return bill
print(get_water_bill(5000))   # 25.0
print(get_water_bill(15000))  # 90.0
print(get_water_bill(25000))  # 175.0
print(get_water_bill(35000))  # 350.0

# phone bill calculation
def get_phone_bill(gb):
    bill = 100
    if gb <=15:
        bill = 100
    else:
        bill = 100+ (gb-15)*100
    return bill
print(get_phone_bill(10))   # 100
print(get_phone_bill(20))   # 500
print(get_phone_bill(30))   # 1000


# LIST
# Do not change: Initial menu for your restaurant
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']



# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu
menu.remove('bean soup')
menu.append('roasted beet salad')

# Customer Avg

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7])/7
avg_last_seven =  sum(num_customers[-7:])/7
max_month = max(num_customers)
min_month = min(num_customers)

# Using name.split to make list from string
# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split(".")
formatted_address = address.split(",")

# Percentage rating
def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

# Number of years 
# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))

# Do not change: Check your answer
