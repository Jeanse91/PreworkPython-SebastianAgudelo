'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

def Total_cuenta (cuenta):
  Total = (cuenta)*1.15
  return (Total)

cuenta = float(input("Introducir importe de la cuenta: "))

print (f"Total a pagar con el 15% de propoina es: {Total_cuenta(cuenta)}€")
