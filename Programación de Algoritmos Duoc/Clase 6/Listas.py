#Listas

#append(valor) agrega un elemento al final de la lista
#extend([]) agrega contenido lista2 al final de la lista
#insert(posicion, valor) agrega un elemento en la posicion especificada
#remove(valor) elimina un elemento de la lista
#pop() o pop(posicion) elimina el ultimo elemento // elimina el elemento de la posicion especificada

#lista.sort(reverse=True) => Ordenar a lista de forma decrescente
#lista.sort() => Ordenarlista de forma crescente
#lista.sort(key=len) = ordena lista con palabras por longitud de menor a mayor
#lista.reverse() => Ordenar lista en reversa

lista = [1, 50, 25, 100, 75]
print("inicial: ", lista)

lista.append(150)
print("append: ", lista)

lista2=[99, 500]
lista.extend(lista2)
print("extend: ", lista)

lista2=[99, 500]
lista.insert(2, 999)
print("insert: ", lista)

list2 = [99, 500]
lista.remove(99)
print("remove: ", lista)

lista2 = [99, 500]
lista.pop(4)
print("pop: ", lista)

