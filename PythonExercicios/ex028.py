'''28 Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''
from time import sleep
from random import randint
c = randint(0, 5)
print('Tenta adivinhar qual número eu pensei no intervalo de 0 e 5')
d = int(input('Qual número que eu escolhi? '))
print('CARREGANDO ....')
sleep(4)
if c == d:
    print('Você acertoou! Parabens! o número foi {}'.format(c))
else:
    print('Você errou, eu ganhei, o número era {}'.format(c))
