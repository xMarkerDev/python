#Calculadora basica usando input
# number1 = float(input("ingresa el primer numero: "))
# number2 = float(input("ingresa el segundo numero: "))

#Operaciones

# suma = number1 + number2
# resta = number1 - number2
# multiplicacion = number1 * number2

#Mostrar resultados

# print("Resultados")

# print(f"Suma: {number1} + {number2} = {suma}")
# print(f"Resta: {number1} - {number2} = {resta}")
# print(f"Multiplicacion: {number1} x {number2} = {multiplicacion}")

# if number2 != 0:
#   division = number1 / number2
#   print(f"Division: {number1} / {number2} = {division}")
# else:
#   print("Division: No se puede dividir entre 0")

#Agregamos ahora menos interactivos

while True:
  print("Calculadora con opciones")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicacion")
  print("4. Division")
  print("5. Exit")
  
  option = input('Elige una opcion del 1-5: ')
  
  if option == "5":
    print("Gracias por usar la calculadora")
    break
  
  if option in ["1", "2", "3", "4"]:
    
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    
    if option == "1":
      resultado = num1 + num2
      print(f"Resultado: {num1} + {num2} = {resultado}")
      
    if option == "2":
      resultado = num1 - num2
      print(f"Resultado: {num1} - {num2} = {resultado}")
      
    if option == "3":
      resultado = num1 * num2
      print(f"Resultado: {num1} x {num2} = {resultado}")
      
    if option == "4":
      
      if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
        
      else:
        print("Resultado: Divisio por cero no definida")
        
  else:
    print("Opcion no valida")