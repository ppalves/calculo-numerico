import math


x0 = 0
x1 = 5
tolerancia = 0.001
count = 0


while abs(x0 - x1) > tolerancia:
    count += 1
    x2 =  ((x0*(x1 - math.exp(-x1))) - (x1*(x0 - math.exp(-x0))))/((x1 - math.exp(-x1)) - (x0 - math.exp(-x0)))
    aux = x1
    x1 =  x2
    x0 = aux     

print(count)
print(x1, x0)