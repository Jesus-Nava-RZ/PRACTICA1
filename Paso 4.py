def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Solicitar número al usuario
try:
    numero = int(input("Introduce un número para calcular su factorial: "))
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Por favor, introduce un número entero válido.")
