#1st problem
# Swapping two Variables.
# - Two numbers will be taken as input and then they will be kept in a variable and displayed.
# - Then the numbers will be swapped and then the changed output will be displayed.
#SOLUTION


a = input()
b = input()
print('a =' +a)
print('b =' +b)
print('After Swapping')
print('a =' +b)
print('b =' +a)



# 2nd Problem
# Solving a Quadratic Equation with Real Solutions.
# Solution


import math
print('input the coefficients a, b ,c sequentially-')
astr = input()
bstr = input()
cstr = input()
a = int(astr)
b = int(bstr)
c = int(cstr)
D = math.sqrt(b*b-4*a*c)
x1 = (-b+D) / (2*a)
x2 = (-b-D) / (2*a)
print(x1)
print(x2)




#3rd Problem
#Converting celcius to farenheit
# Input will take a celcius temperature and will convert to farenheit and will give us the output.
## SOLUTION


print('celcious temperature-')
C = input()
c = float(C)
F = 9/5 * c + 32
print('Farenheit Temperature is-')
print(F)
