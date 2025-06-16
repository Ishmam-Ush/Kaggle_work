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

