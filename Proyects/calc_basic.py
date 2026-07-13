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

#Funciones

def menu ():
  print("Calculadora con opciones")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicacion")
  print("4. Division")
  print("5. Historial")
  print("6. Exit")

def sumar (a, b):
  return a + b

def restar (a, b):
  return a - b

def mutiplicar (a, b):
  return a * b

def dividir (a, b):
  if num2 == 0:
    return print("Resultado: Division por 0 NO definida")
  else:
    return a / b

def definir_numeros ():
  while True:
    try:
      n1 = float(input("Ingresa el primer numero: "))
      n2 = float(input("Ingresa el segundo numero: "))
      return n1, n2
    except ValueError:
      print("Error: Ingresa numeros validos")

historial = []

while True:
  menu()
  option = input('Elige una opcion del 1-6: ')
  
  if option == "6":
    print("Gracias por usar la calculadora")
    break
  
  elif option == "5":
    if historial:
      print("HISTORIAL")
      for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")
    else:
      print("No hay operaciones en el historial")
  
  
  elif option in ["1", "2", "3", "4"]:
    
    num1, num2 = definir_numeros()
    
    if option == "1":
      resultado = sumar(num1,num2)
      operacion = f"{num1} + {num2} = {resultado}"
      
    elif option == "2":
      resultado = restar(num1,num2)
      operacion = f"{num1} - {num2} = {resultado}"
      
    elif option == "3":
      resultado = mutiplicar(num1,num2)
      operacion = f"{num1} * {num2} = {resultado}"
    
    elif option == "4":
      resultado = dividir(num1,num2)
      if num2 == 0:
        operacion = "Operacion no definida"
      else:
        operacion = f"{num1} / {num2} = {resultado}"
        
    print(f"{operacion}")
    historial.append(operacion)
    
  else:
    print("Opcion no valida")