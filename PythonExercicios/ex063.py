'''
63 Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonacci.
Ex
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
n = int(input('Digite um número inteiro: '))
print('Sequência de Fibonacci do número {} ficou: '.format(n))
print('#' * 90)
t = 0
t1 = 1
print('{} \33[31m ==> \33[33m {}'.format(t, t1), end='')
con = 3
while con <= n:
    t2 = t + t1
    print('\33[31m ==> \33[33m {}'.format(t2), end='')
    t = t1
    t1 = t2
    con += 1
print('\33[31m ==> # FIM # \33[m')
print('#' * 90)