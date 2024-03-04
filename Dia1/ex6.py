#Faca um programa que pergunte um numero e diga se ele é primo ou não: 

numero = int(input('escolha um numero : '))
resto = numero % 2

if numero == 1 :
    print('esse numero não é primo')
elif resto == 0 :
    print('Esse numero não é primo')
else: 
    print('Esse numero é primo')