'''31 Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM
e R$0,45 para viagens mais longas'''
d = float(input('Qual a distância da viagem em KM? '))
p =  d * 0.50
p1 = d * 0.45
if d > 200:
    print('Você viagou {} KM, portanto irá pagar R${}'.format(d, p1))
else:
    print('Você viajou {} KM, portanto irá pagar R${:.2f} '.format(d, p))