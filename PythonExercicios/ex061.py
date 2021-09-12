'''
61 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''
'''Exercicio 51 com for '''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
con = 1
while con <= 10:
    print('{} \33[31m ==> \33[33m'.format(termo), end='')
    termo += r
    con += 1
print('\33[31m # FIM #\33[33m')

