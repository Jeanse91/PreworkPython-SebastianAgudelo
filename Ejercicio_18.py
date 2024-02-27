'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

contador=0
frase= str(input("Introduce una frase: "))
palabras= frase.split(" ")

for palabra in palabras:
  contador += 1
print (contador)