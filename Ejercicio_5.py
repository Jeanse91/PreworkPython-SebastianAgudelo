'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

suma_total=0
for par in range(1,101):
  if par % 2 == 0:
    suma_total += par

print ("La suma de todos los numero pares de 1 a 100 es,",suma_total)