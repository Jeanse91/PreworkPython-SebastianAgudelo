'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.''' 

def imc (peso, estatura):
  return (peso) / (estatura*estatura)

peso= float(input("Introduzca su peso en kg: "))
estatura = float(input("Introduzca su estatura en metros: "))

print (imc(peso, estatura))
