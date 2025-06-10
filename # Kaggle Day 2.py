# Kaggle Day 2

# If statement (Fever exp)
def evaluate(temp):
    message = "normal temperature"
    if temp > 40:
        message = "High fever"
        return message
print(evaluate(41))  # High fever
