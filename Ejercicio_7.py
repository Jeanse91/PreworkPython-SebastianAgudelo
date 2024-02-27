'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

def suma (numero1, numero2):
  return numero1 + numero2
def resta (numero1, numero2):
  return numero1 - numero2
def multiplicacion (numero1, numero2):
  return numero1 * numero2
def division (numero1, numero2):
  return numero1 / numero2

opcion = input("Que oprecion desea realizar. Suma, Resta, Multiplicaciòn o división: ")

if opcion == "Suma":
  numero1= float(input("Introduzca el primer numero: "))
  numero2= float(input("Introducir el segundo número: "))
  print (suma(numero1, numero2))

elif opcion == "Resta":
  numero1= float(input("Introduzca el primer numero: "))
  numero2= float(input("Introducir el segundo número: "))
  print (resta(numero1, numero2))

elif opcion == "Multiplicación":
  numero1= float(input("Introduzca el primer numero: "))
  numero2= float(input("Introducir el segundo número: "))
  print (multiplicacion(numero1, numero2))

elif opcion == "División":
  numero1= float(input("Introduzca el divisor: "))
  numero2= float(input("Introducir el dividendo: "))
  print (division(numero1, numero2))

else:
  print ("Operación no disponible.")