'''35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo'''
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('O comprimento dessas três retas pode formar um triângulo')
else:
    print('Infelizmente não pode formar um triângulo')

