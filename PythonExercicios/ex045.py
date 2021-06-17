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
                     '0 - PEDRA\n'
                     '1 - PAPEL\n'
                     '2 - TESOURA\n'
                     'ESCOLHA:  '))
print('JOKEENNN PÔ  ...')
sleep(3)
print('Jokenpô escolheu "{}"'.format(po[joke]))
print('Você escolheu "{}"'.format(po[escolhas]))
if joke == 0:
    if escolhas == 0:
        print('EMPATE')
    elif escolhas == 1:
        print('VOCÊ VENCEU')
    elif escolhas == 2:
        print('PERDEU')
    else:
        print('Opção inválida')
elif joke == 1:
    if escolhas == 0:
        print('PERDEU')
    elif escolhas == 1:
        print('EMPATE')
    elif escolhas == 2:
        print('VOCÊ VENCEU')
    else:
        print('Opcão inválida')
elif joke == 2:
    if escolhas == 0:
        print('VOCÊ VENCEU')
    elif escolhas == 1:
        print('PERDEU')
    elif escolhas == 2:
        print('EMPATE')
    else:
        print('Opção inválida')