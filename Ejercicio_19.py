'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''

año= int(input("Introduce año a comprobar: "))

if año % 4 ==0 and año %100 != 0:
  print (f"{año} es un año bisiesto")
elif año % 4==0 and año % 100 == 0 and año % 400 == 0:
  print (f"{año} es un año bisiesto")
elif año % 4==0 and año % 100 == 0 and año % 400 != 0:
  print (f"{año} no es un año bisiesto")
elif año % 4 != 0:
  print (f"{año} no es un año bisiesto")