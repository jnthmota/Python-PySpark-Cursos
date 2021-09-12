'''
60 Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex
5! = 5x4x3x2x1 = 120
FOR e While
'''
from math import factorial
from time import sleep
n = int(input('Digite um número: '))
f = factorial(n)
print('#' * 40)
print('O factorial de {} é {}'.format(n, f))
print('#' * 40)

'''using while'''
n = int(input('Digite um número: '))
con = n
f = 1
print('\33[31mCalculando [{}]....\33[33m'.format(n))
while con > 0:
    print('{}'.format(con), end='')
    print(' x ' if con > 1 else ' = ', end='')
    f *= con
    con -= 1
print('{}'.format(f))
print('\33[31m#' * 7)
print('# FIM #')
print('#' * 7)
