#Cual es el numero mayor o menor

def main():
    Num = []
    print ("Introduce los numeros que desee para poder compararlos.")
    print ("Compararemos cual es el mayor o el menor de todos los numeros que nos proporcione")
    print ("Cuando crea necesario introduzca 'salir' para finalizar el programa y dar el resultado")
    print("")
    print("----------------------------------------------------------------------------------------")

    while True:
      Entrada = input("Introduce un número que quieras (o 'salir' si has terminado): ").strip()
      if Entrada.lower() == 'salir':
         break
      try: 
         Nu = float(Entrada)
         Num.append(Nu)
      except ValueError:
         print("El numero no es valido, favor de introducior otro: ")
    
    if Num:
     print("\nRESULTADOS: ")
     print(f"El numero maximo es: {max(Num)}")
     print(f"El numero minimo es: {min(Num)}")
     print(f"La cantidad de numeros ingresados fueron: {len(Num)}")
    else:
     print("No ha ingresado ningun numero,ingreselo, por favor. ")
 
main()

     
    