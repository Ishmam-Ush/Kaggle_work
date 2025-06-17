# Loops and list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=', ')
    #print(planet)   # The above code prints each planet twice, once with a comma and once on a new line.

print()  # This code prints each results on a new line.

# multiplicands
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product*mult
product # The above code calculates the product of the multiplicands.
print(product)

# list comprehension 
