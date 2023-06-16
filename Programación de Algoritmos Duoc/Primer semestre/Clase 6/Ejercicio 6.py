#Cree una lista para almacenar nombres. El proceso se realiza preguntando si desea seguiringresando. Si la respuesta es NO, se detiene el proceso.Luego, elimine el nombre con la menor cantidad de caracteres.

lista = []

opcion = "si"

while opcion!= "no":
    nombre = input("Ingrese su nombre: ")
    lista.append(nombre)
    opcion = input("Desea seguir ingresando nombres? \n Si \n No \n").lower()

lista.sort(key(len))
lista.pop(0)
print(lista)
