'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

dia = int(input("Introducir el número de día: "))

if dia == 1:
  print ("EL día 1 de la semana es Lunes.")
elif dia ==2:
  print ("El día 2 de la semana es el Martes.")
elif dia == 3:
  print ("El día 3 de la semana es el Miércoles.")
elif dia == 4: 
  print ("El día 4 de la semana es el Jueves.")
elif dia ==5: 
  print ("El día 5 de la semana es Viernes.")
elif dia == 6:
  print ("El día 6 de la semana es el Sábado.")
elif dia ==7: 
  print ("El día 7 de la semana es Domingo.")
else:
  print ("La semana solo tiene 7 días.")
