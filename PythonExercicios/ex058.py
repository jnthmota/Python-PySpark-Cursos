'''
58 Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''
from time import sleep
from random import randint
c = randint(0, 10)
d = ''
while d != c:
    d = int(input('Qual número eu escolhi? '))
    print('\33[32mPROCESSANDO ...\33[m')
    sleep(1)
    if c == d:
        print('Você \33[34m"ACERTOU"\33[m, Parabeéns!! o número foi {}!'.format(c))
    else:
        print('Você \33[31m"ERROU"\33[m tente novamente!')
        print('-=-' * 10)
print('-=-' * 10)

