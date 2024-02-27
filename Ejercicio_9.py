'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''

'''dolar= float(input("Introducir importe en dolares: "))

euros = (dolar) * 0.85

print (f"{dolar} dolares son {euros} euros")'''

def dolar_euro (dolar, euro):
  return dolar * euro

euro= float(input(f"Introducir importe en dolares: "))
dolar=0.85
print (f"{euro} dolares son {dolar_euro(dolar, euro)} euros")