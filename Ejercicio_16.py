'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

lista = [ ]
pares= 0
impares = 0
numeros = int(input("Introduce número para añadir a la lista y 0 para terminar la lista: "))
while numeros != 0:
  lista.append(numeros)
  numeros = int(input("Introduce número para añadir a la lista y 0 para terminar la lista: "))
for numero in lista:
    if numero %2==0:
      pares += 1
    else:
      impares += 1
print (f"Hay {pares} números pares y {impares} números impares.")

print (lista)