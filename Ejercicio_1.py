'''Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.'''

def F_degrees (Celcius):
  f = (Celcius*9/5) + 32,
  return f

Celcius=float(input("introduzca los grados en Cº: "))

print (f"{Celcius} grados celcius son {F_degrees(Celcius)} grados fahrenheit.")

