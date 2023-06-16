import numpy as np

#Lista
lista = [[1,2,3],[4,5,6],[7,8,9]]
print(lista)

arreglo = np.array(lista)
print(arreglo)
print(arreglo[1,1])

#Reshape =
arreglo2 = np.arange(80,101).reshape((51,52,43))
print(arreglo2)

for y in range(10):
    for x in range(10):
        print(arreglo[y,x])


arr1 = np.array([[1,2,3],[4,5,6])
arr2 = np.array([[10,20,30],[40,50,60]])
arr3 = np.concatenate((arr1,arr2),axis=0)
print(arr3)