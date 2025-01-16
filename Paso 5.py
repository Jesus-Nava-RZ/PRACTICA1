#TABLA DE MULTIPLICAR DEL 1 AL 10

Nu = int(input("Por favor, escriba la tabla que desea ver (Solo es posible las tablas del 1 al 10): "))
 
if(Nu >1 and Nu <11):
  for I in range(0, 11):
   Resul = I * Nu
   print(Nu, " X ",I," = ",Resul)

else:
 print("NO es posible multiplicar numeros negativos o el cero. ")
 print("NO es posible multiplicar despues del numero once. ")
 print("POR FAVOR, SELECCIONES UN NUMERO DEL UNO AL DIEZ.")