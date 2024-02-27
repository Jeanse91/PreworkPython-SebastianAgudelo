'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''

lista = [ ]
suma=0
numeros = int(input("Introduce el número que quieres añadir a la lista y 0 para terminar la lista: "))
while numeros != 0:
  lista.append(numeros)
  numeros = int(input("Introduce el número que quieres añadir a la lista y 0 para terminar la lista: "))
for numero in lista:
  suma += numero
print (f"La suma de tu lista es: {suma}.")

print (lista)