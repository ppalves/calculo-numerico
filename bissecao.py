import math

a = 0
b = 1

while abs(a - b) > 0.001:
    print("[ " + str(a) + " , [ " + str(b) + " ]")
    x = (a+b)/2
    if (math.cos(x) - x) > 0:
        a = x
    else:
        b = x

print("=========")
print(a,b)