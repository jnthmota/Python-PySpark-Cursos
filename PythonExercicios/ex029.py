'''29 Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite.'''
v = float(input('Qual é a velocidade do carro? '))
m = (v - 80) * 7
if v > 80:
    print('Voce está há {} KM ultrapassando o limite de 80KM velocidade. \n'
          'Foi MULTADO em R${}'.format(v, m))
else:
    print('Você esta há {} KM portanto não ultrapassou o limite de velocidade'.format(v))
    print('Boa Viagem!')
