'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.'''

'''numero = int(input("Introduce un número entero mayor a 1: "))

if numero < 2:
  print (f"{numero} NO es un número primo.")
elif numero==2:
  print (f"{numero} Si es un número primo")
elif numero % 2==0: 
  print (f"{numero} NO es un número primo.")
elif numero % numero == 0:
  print (f"{numero} SI un número primo.")'''

def es_primo(numero):
  if numero<2:
    return (f"{numero} NO es un numero primo")
  for i in range(2, numero):
     if (numero % i)== 0:
        return (f"{numero} NO es un número primo.")
  return (f"{numero} SI es un número primo.")

numero= int(input("Introduce un número: "))
print (es_primo(numero))
