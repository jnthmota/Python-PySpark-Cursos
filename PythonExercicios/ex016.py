#16 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
n = float(input('Digite um número: '))
print('O número {} tem a parte Inteira de {}'.format(n, trunc(n)))
