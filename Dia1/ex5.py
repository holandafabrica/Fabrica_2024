# faca um programa que pergunte um numero e diga se ele é impar ou par

numero = int(input('escolha um numero : '))
resto = numero % 2

if resto == 0:
    print('Esse numero é par')
else:
    print('Esse numero é impar')
  