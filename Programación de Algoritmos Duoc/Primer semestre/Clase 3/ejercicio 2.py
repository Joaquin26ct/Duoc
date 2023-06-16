#Ingrese por teclado 10 letras, indique cuantas de ellas son vocales y cuántas son consonantes

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vocales_contador = 0
consonantes = 0

for i in range(10):
    letras = input("ingrese una letra: ")
    if letras in vocales:
        vocales_contador += 1
    else:
        consonantes += 1
print(f"Hay {vocales_contador} vocales y {consonantes} consonantes. ")
