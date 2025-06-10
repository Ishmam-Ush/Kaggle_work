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
