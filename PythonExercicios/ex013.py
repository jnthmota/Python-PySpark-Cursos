#13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual e seu salário atual? R$'))
r1 = (s / 100) * 115
print('O reajuste de 15% no seu salário atual de R${}, passará a ser de R${}'.format(s, r1))