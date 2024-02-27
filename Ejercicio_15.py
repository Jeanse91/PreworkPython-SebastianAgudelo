'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

def horas_minutos (minutos):
  horas=0
  resto_minutos=0
  if minutos >= 60:
      horas = minutos // 60
      resto_minutos = minutos % 60
  else:
    horas=0
    resto_minutos=minutos
  return (f"{horas} horas, {resto_minutos} minutos.")

minutos= int(input("Introducir cantidad de minutos: "))
print (horas_minutos(minutos))