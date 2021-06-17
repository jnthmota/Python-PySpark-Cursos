'''
45 Crie um programa que faça o computador jogar Jokenpô com você.
'''
from time import sleep
from random import randint
print('JOKENPÔ')
print('-=-' * 20)
po = ('Pedra', 'Papel', 'Tesoura')
joke = randint(0, 2)
escolhas = int(input('Faça uma escolha: \n'
                     '1 - PEDRA\n'
                     '2 - PAPEL\n'
                     '3 - TESOURA\n'
                     'ESCOLHA:  '))
print('VALIDANDO ESCOLHAS  ...')
sleep(3)
print('Jokenpô escolheu {}'.format(po[joke]))
print('Você escolheu {}'.format(po[escolhas]))