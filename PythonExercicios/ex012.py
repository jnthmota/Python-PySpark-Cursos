#12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual é o preço do produto? R$'))
r1 = (p / 100) * 95
print('O valor de R${} com 5% de desconto será de R${}'.format(p, r1))