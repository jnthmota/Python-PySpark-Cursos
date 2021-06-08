#10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
d = float(input('Quanto dinheiro você tem em R$? '))
r1 = d / 5.05
print('Você pode comprar com R${}, cerca de ${:.4} dólares'.format(d, r1))