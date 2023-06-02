#Crear una lista con números enteros positivos aleatorios entre 1 y 100, luego muestre el número menor y el mayor.

import random

lista = []
for i in range(30):
    lista.append(random.randint(1,100))

print(lista)
lista.sort
print(lista)
print(f"El menor número es {lista[0]}")
print(f"El mayor número es {lista[-1]}")