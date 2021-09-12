'''
65 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o MAIOR e o MENOR valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
continuar = 'S'
soma = qt = md = maior = menor = 0
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    qt += 1
    if qt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
                menor = n
    continuar = str(input('Quer continuar ? \n'
                          '[ S ] sim\n'
                          '[ N ] não\n'
                          ' ')).upper().strip()[0]
md = soma / qt
print('Você digitou {} números e a média de todos eles foi {}'.format(qt, md))
print('O MAIOR número foi {} e o MENOR foi {}'.format(maior, menor))
print('\33[31m#' * 7)
print('# FIM #')
print('#' * 7)