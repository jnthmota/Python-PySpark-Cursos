'''33 Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR'''
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a > b and a > c:
    maior = a
    print('-' * 40)
    print('O número {} é MAIOR que {} e {}'.format(maior, b, c))
if b > a and b > c:
    maior = b
    print('O número {} é MAIOR que {} e {}'.format(maior, a, c))
    print('-' * 40)
if c > a and c > b:
    maior = c
    print('O número {} é MAIOR que {} e {}'.format(maior, a, b ))
    print('-' * 40)
if a < b and a < c:
    menor = a
    print('O número {} é MENOR que {} e {}'.format(menor, b, c))
    print('-' * 40)
if b < a and b < c:
    menor = b
    print('O número {} é MENOR que {} e {}'.format(menor, a, c))
    print('-' * 40)
if c < a and c < b:
    menor = c
    print('O número {} é MENOR que {} e {}'.format(menor, a, b))
    print('-' * 40)




