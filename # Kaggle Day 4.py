# Lists
num = [1,2,3,4,5,6,7,8,9,10]
print(num[0])
print(num[-1])
print(num[-2])
# Slicing
print(num[:2])
print(num[0:3])
print(num[3:])
print(num[1:-1])
print(num[-4:])
#num[3]= "X"
#print(num)
#num[3:5] = ["X", "Y"]
#print(num)

print(len(num))
print(sorted(num))
# print(num.count(1))
print(sum(num))
print(min(num))
print(max(num))
# print(num.index(1))

x = 2
print(x.imag)
c  = (2+2j)
print(c.imag)
print(c.real)
print(c)
# Interlude
print(x.bit_length())
print(num.append(11))
print(num)
print(num.pop(2))
print(num)
print(num.index(6)) # Helps finding place of an object in a list
x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator/denominator)

# classic swap 
a = 1
b = 0
a, b = b, a
print(a,b)

# Exercise 1

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    
    return L[1]

# Exercise 2

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

# Exercise 3 [mario purple shell swap]
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0],racers[-1] = racers[-1],racers[0]
    return racers
print(purple_shell(["Mario", "Bowser", "Luigi"]))

# Exercise 4 Length of Lists
# In this exercise, we will predict the lengths of several lists.
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3,2,0,2]

# Exercise 5
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals)/2 and order != len(arrivals)-1
