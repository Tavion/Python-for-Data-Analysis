import numpy as np
a0 = float(input("The first item is: "))
q = float(input("The proportion is: "))
n = int(input("The number of items is: "))

item = np.zeros((1, n))
ai = a0
suma = 0
for i in np.arange(n):
    item[0][i] = ai
    ak = ai*(1+q)
    ai = ak
    suma += ak
print(i)
arr = item.reshape((73,5))
print(arr)

print(suma)

