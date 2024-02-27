'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

palabra = input("Introducir palabra: ")
if palabra == palabra [::-1]:
  print (f"{palabra} es un palindromo")
else:
  print (f"{palabra} no es un palindromo")