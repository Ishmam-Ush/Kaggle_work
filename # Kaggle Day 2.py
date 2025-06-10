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