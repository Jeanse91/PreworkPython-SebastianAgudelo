'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

def vocales (Total_vocales):
  Total= 0
  for Vocal in Total_vocales:
    if Vocal in "aeiouAEIOU":
      Total += 1
  return Total 

Total_vocales = input("Introducir palabra: ")
print (f"Hay {vocales(Total_vocales)} vocales")
