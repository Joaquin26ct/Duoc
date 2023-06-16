#Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema debe mostrar por pantalla el nombre que tenga mayor cantidad de caracteres.
lista = []

for i in range(3):
    palabra = input("Ingrese una palabra: ")
    lista.append(palabra)

print(lista)
lista.sort(key=len)
print(f"La palabra con mas letras es {lista[-1]}")