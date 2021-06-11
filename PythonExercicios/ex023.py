'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados'''
l = int(input('Digite um número de 0 a 9999: '))
a = l // 1 % 10
b = l // 10 % 10
c = l // 100 % 10
d = l // 1000 % 10
print('Você digitou {} '.format(l))
print('-'*50)
print ('Quarto número: {}\nTerceiro múmero: {}\nSegundo número: {}\nPrimeiro número: {}'\
      .format(a, b, c, d))