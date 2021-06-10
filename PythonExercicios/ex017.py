'''17 Façã um programa que leia o comprimento do cateto aposto e do cateto adjacente de um triângulo
 retângulo, calcule e mostre o comprimento da hipotenusa. '''
from math import hypot
cp = float(input('Digite o comprimento do cateto aposto: '))
ca = float(input(('Digite o comprimento do cateto adjacente: ')))
h = hypot(cp, ca)
print('=' * 50)
print('O comprimento do cateto aposto {} \n O comprimento do cateto adjacente {}.'.format(cp, ca))
print('=' * 50)
print('Vai resultar na hipotenusa de {:.2f}'.format(h))