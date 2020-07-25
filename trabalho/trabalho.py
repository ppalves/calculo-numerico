import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")
values = data.values
x = values[:,0]
fx = values[:,1]

def produto_interno(array1, array2):
    return sum([a * b for a,b in zip(array1, array2)])

a00 = produto_interno(np.ones(63),np.ones(63))
a01 = produto_interno(np.ones(63),x)
a10 = produto_interno(x,np.ones(63))
a11 = produto_interno(x,x)
f1 = produto_interno(fx, np.ones(63))
fx = produto_interno(fx, x)
print("Dados:")
print(a00)
print(a01)
print(a10)
print(a11)
print(f1)
print(fx)
# a = np.array([])
# print(produto_interno([1,2,3], [1,2,3]))

# def funcao(x): 
#     return x**2

# mappado = map(funcao, [1,2,3])

# print(list(mappado))


a = np.array([[a00,a01],[a10,a11]])
b = np.array([f1,fx])
x = np.linalg.solve(a,b)
print(x)