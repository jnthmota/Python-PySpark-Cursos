'''30 Cria um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR'''
nr = int(input('Digite um número: '))
n = nr % 2
if n == 0:
    print('O número {} é PAR'.format(nr))
else:
    print('O número {} é IMPAR'.format(nr))