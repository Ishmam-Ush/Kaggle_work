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
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')
# range
for i in range(6):
    print('doing the work i=', i) # repeats the line 6 times with values assigned to i (0-6) and stating each time the value of i taken from range

# while loop
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increment i by 1
print()  # This prints a new line after the while loop output.

# use of  list comprehension
squares = [n**2 for n in range(10)]
squares  # This creates a list of squares of numbers from 0 to 9.
print(squares)

#print()  # This prints a new line after the list comprehension output.
# without list comprehension
aquares = []
for n in range(10):
    squares.append(n**2)

print(squares)  # This appends the square of each number from 0 to 9 to the list squares and prints it.

# use of if in loop
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)
# This returns string all caps
long_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6 ]
print(long_planets)
