#Calculadora basica usando input
number1 = float(input("ingresa el primer numero: "))
number2 = float(input("ingresa el segundo numero: "))

#Operaciones

suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2

#Mostrar resultados

print("Resultados")

print(f"Suma: {number1} + {number2} = {suma}")
print(f"Resta: {number1} - {number2} = {resta}")
print(f"Multiplicacion: {number1} x {number2} = {multiplicacion}")

if number2 != 0:
  division = number1 / number2
  print(f"Division: {number1} / {number2} = {division}")
else:
  print("Division: No se puede dividir entre 0")

