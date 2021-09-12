'''
59 Crie um programa que leia dois valores e mostre um MENU na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2ª valor : '))
opt = 0
while opt != 5:
    print('[ 1 ] Somar \n'
          '[ 2 ] Multiplicar \n'
          '[ 3 ] Maior \n'
          '[ 4 ] Novos números \n'
          '[ 5 ] Sair do programa')
    opt = int(input('Qual é sua escolha ? '))
    if opt == 1:
        soma = n1 + n2
        print('#' * 30)
        print('A soma dos valores é {}'.format(soma))
        print('#' * 30)
    elif opt == 2:
        multiplicar = n1 * n2
        print('#' * 30)
        print('A multiplição do {} mais {} é {}'.format(n1, n2, multiplicar))
        print('#' * 30)
    elif opt == 3:
        if n1 > n2:
            print('#' * 30)
            print('O maior entre os valores é {}'.format(n1))
            print('#' * 30)
        else:
            print('#' * 30)
            print('O maior entre os valores é {}'.format(n2))
            print('#' * 30)
    elif opt == 4:
        print('#' * 30)
        print('Digite os números novamente: ')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2ª valor : '))
        print('#' * 30)
    elif opt == 5:
        print('#' * 30)
        print('\33[34m Encerrando programa ... \33[m')
        print('#' * 30)
        sleep(2)
    else:
        print('#' * 30)
        print('\33[31mOpção inválida digite novamente!\33[m')
        print('#' * 30)
print('\33[31m#' * 7)
print('# FIM #')
print('#' * 7)

