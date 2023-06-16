#Cree 2 listas, en las cuales se guardarán 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos). El sistema deberá mostrar de forma ordenada los nombres y apellidos.

nombres = []
apellidos = []

for i in range(3):
    nombres.append(input("Ingrese el nombre: "))
    apellidos.append(input("Ingrese el apellido: "))

print(nombres)
print(apellidos)