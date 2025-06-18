# Strings and Dictionaries
# single quote character inside a single quoted string
x = 'Pluto\'s a planet!' # backslashing lets us do this
print(x)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)

print("hello")
print("world") # this prints on a new line by default 
print("hello", end='') # end='' prevents a newline  
print("pluto", end='') 

planet = 'Pluto'
# list comprehension to add '!' after each character in planet      
[char+'! ' for char in planet] # for every character in planet add '!' after it and a space 

# A major way in which they differ from lists is that they are IMMUTABLE. We can't modify them.

print()

Planet = 'Pluto'
# String methods
claim = "Pluto is a planet!"
print(claim.upper())
print(claim.lower())
print(claim.title()) # capitalizes the first letter of each word
print(claim.replace('planet', 'dwarf planet')) # replaces 'planet' with 'dwarf planet'
print(claim.split()) # splits the string into a list of words
print(claim.split(' ')) # splits the string into a list of words using space as the delimiter
print(claim.split(' ', 2)) # splits the string into a list of words using space as the delimiter, but only splits at the first two spaces
print(claim.splitlines()) # splits the string into a list of lines
print(claim.startswith('Pluto')) # checks if the string starts with 'Pluto'
print(claim.endswith('planet!')) # checks if the string ends with 'planet!'
print(claim.find('planet')) # finds the index of 'planet' in the string, returns -1 if not found
print(claim.index('planet')) # finds the index of 'planet' in the string, raises ValueError if not found
print(claim.count('a')) # counts the number of times 'a' appears in the string
print(claim.isalpha()) # checks if the string contains only alphabetic characters
print(claim.isalnum()) # checks if the string contains only alphanumeric characters
print(claim.isdigit()) # checks if the string contains only digits


datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)  # prints the year, month, and day as separate variables

'/'.join([month, day, year])
print('/'.join([month, day, year]))  # joins the month, day, and year with '/' as the delimiter

# Calling non string objects as strings
position = 9
planet + ", you'll always be the " + str(position) + "th planet to me." # Have to define using str() to convert position to a string
print(planet + ", you'll always be the " + str(position) + "th planet to me.")  # Concatenates strings and prints
# using .format() method for cleaner string formatting
"{}, you'll always be the {}th planet to me.".format(planet, position) # inside format we define the placeholders respectively to the curly brackets
print("{}, you'll always be the {}th planet to me.".format(planet, position))  # Concatenates strings and prints using .format()

# .format() magic
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,) # use of .format() we can set decimal points, format as percent, and separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,))  # Concatenates strings and prints using .format()

# From format() , using indexes to refer to the arguments 
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

### Dictionaries 
# these are used to map keys to values
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

# we can change values add another key 
numbers['eleven'] = 11
numbers['one']= 'pluto'
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets} # what happens here is we call planet and its first index from the list of planets
print(planet_to_initial, sep='\n')

# USE of in operator for checking the abvailability of any variables, returns bool
print('Saturn' in planet_to_initial)
print('IO' in planet_to_initial)

# for loop over dictionary
for k in numbers:
    print("{} = {}".format(k,numbers[k]))

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))

# rjust 
for planet ,initial in planet_to_initial.items():
    print("{}\'begins with' \"{}\"".format(planet.rjust(10), initial))