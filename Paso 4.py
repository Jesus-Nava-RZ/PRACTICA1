def main():
    numeros = []
    print("Introduce números. Escribe 'salir' para terminar.")

    while True:
        entrada = input("Introduce un número (o 'salir'): ").strip()
        if entrada.lower() == 'salir':  # Si el usuario escribe 'salir', termina el bucle
            break
        try:
            numero = float(entrada)  # Convierte la entrada en número
            numeros.append(numero)   # Agrega el número a la lista
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Verifica si se ingresaron números antes de calcular resultados
    if numeros:
        print("\nResultados:")
        print(f"Valor máximo: {max(numeros)}")
        print(f"Valor mínimo: {min(numeros)}")
        print(f"Total de valores ingresados: {len(numeros)}")
    else:
        print("No se ingresaron números.")

# Llamada a la función principal
main()
