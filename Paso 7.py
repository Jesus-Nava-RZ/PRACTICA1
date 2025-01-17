print("Paso 7. Determinación del promedio (media) de una serie de números. ")
print("El programa debe dejar de aceptar valores cuando se indique el valor -1.")
print("")

def ca_Promedio():
    print("Introduce varios numeros para calcular el promedio. Ingresa -1 para terminar ")
    Numeros = []
    while True:
        try: 
            Numero = float(input("Numero: "))
            if Numero == -1:
                break
            Numeros.append(Numero)
        except ValueError:
            print("Por favor, introduzca un numero valido.")
    if Numeros:
        Promedio = sum(Numeros)/len(Numeros)
        print(f"El promedio final es: {Promedio}")
    else:
        print("Algunos de los numeros introducidos no son validos para calcular el promedio.")
ca_Promedio()

