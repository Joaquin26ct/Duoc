#Considere la lista del ejercicio 1 y genere una segunda lista con los elementos ordenadosen forma ascendente y una tercera lista con los elementos ordenados descendentemente.Mostrar los tres resultados

lista = []

for i in range(1,11):
    lista.append(5*1)

lista2 = lista.copy()
lista2.sort()

lista3 = lista2.copy()
lista3.sort(reverse=True)

print(lista)
print(lista2)
print(lista3)
