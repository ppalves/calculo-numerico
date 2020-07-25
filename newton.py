import math

x = float(input())

for i in range(10):
    x1 = x - ((math.cos(x) - x)/((-math.sin(x)) - 1 )) 
    x = x1
    print(x)

print("---")
print(x)