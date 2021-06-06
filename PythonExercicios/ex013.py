# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO

s = float(input('Qual e seu salário atual? '))
r1 = (s / 100) * 115
print('O reajuste de 15% no seu salário atual de R${}, passará a ser de R${}'.format(s, r1))