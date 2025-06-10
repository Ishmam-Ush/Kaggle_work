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