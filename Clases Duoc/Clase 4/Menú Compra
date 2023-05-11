opcion = 0
total = 0

while opcion!= 5:
    try:
        print("Menu de compra ")
        print("1. Pan amasado $1.500 ")
        print("2. Molde $1.000 ")
        print("3. Baguette $2.000")
        print("4. Integral $3.000 ")
        print("5. Terminar Compra")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            cantidad = int(input("cuantos desea: "))
            total +=(1500*cantidad)
        elif opcion == 2:   
            cantidad = int(input("cuantos desea: "))
            total +=(1000*cantidad)
        elif opcion == 3:   
            cantidad = int(input("cuantos desea: "))
            total +=(2000*cantidad)
        elif opcion == 4:   
            cantidad = int(input("cuantos desea: "))
            total +=(3000*cantidad)
        elif opcion == 5:
            if total>5000:
                print(f"El total a pagar es ${total}")
            else:
                total+=(total*0.1)
                print(f"El total a pagar es ${total}")
        else:
            print("Ingrese una opcion valida")
    except ValueError:
        print("Ingrese un numero valido")
    except:
        print("Invalido")
