'''
64 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(Desconsiderando o flag)
'''
n = con = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    print('[999] para parar')
    soma += n
    con += 1
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma deles foi {}'.format(con, soma))
print('\33[31m#' * 7)
print('# FIM #')
print('#' * 7)