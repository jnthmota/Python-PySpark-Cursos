#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR

d = float(input('Quanto dinheiro você tem em R$? '))
r1 = d / 5.05
print('Você pode comprar com R${}, cerca de ${:.4} dólares'.format(d, r1))