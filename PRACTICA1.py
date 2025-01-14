def suma_numeros():
    n = int(input("¿Cuántos números deseas sumar? "))
    total = 0
    for i in range(n):
        num = float(input(f"Ingresa el número {i+1}: "))
        total += num
    print(f"La suma total es: {total}")

def producto_numeros():
    n = int(input("¿Cuántos números deseas multiplicar? "))
    total = 1
    for i in range(n):
        num = float(input(f"Ingresa el número {i+1}: "))
        total *= num
    print(f"El producto total es: {total}")

def division_numeros():
    num1 = float(input("Ingresa el primer número (dividendo): "))
    num2 = float(input("Ingresa el segundo número (divisor): "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Suma de 'n' números")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            suma_numeros()
        elif opcion == '2':
            producto_numeros()
        elif opcion == '3':
            division_numeros()
        elif opcion == '4':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()