#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO
p = float(input('Qual é o preço do produto? R$'))
r1 = (p / 100) * 95
print('O valor de R${} com 5% de desconto será de R${}'.format(p, r1))