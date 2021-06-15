'''
36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa. o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
negado.
'''
from time import sleep
a = float(input('Qual e o valor da casa? '))
b = float(input('Qual é seu salário? '))
c = int(input('Quantos anos você pretende pagar? '))
p = a / (c * 12)
m = b * 30 / 100
print('A casa irá custar R$:{} em {} anos\n'
      'Com prestação no valor de R$:{}'.format(a, c, p))
print('ANALISANDO INFORMAÇÔES ...')
sleep(3)
print('-=-'*20)
if p <= m:
    print('Emprestimo "APROVADO!"')
else:
    print('Emprestimo "NEGADO!"')


