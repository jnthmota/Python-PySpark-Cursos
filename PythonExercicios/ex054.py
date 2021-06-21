'''
54 Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
Quantas já são maiores a partir dos 21 anos.
'''
from datetime import date
a = date.today().year
mr = 0
mn = 0
for c in range(1,8):
    l = int(input('Qual ano de nascimento da {}° pessoa?  '.format(c)))
    idade = a - l
    if idade >= 21:
        mr += 1
    else:
        mn += 1
print('-=-' * 20)
print('Houveram \33[31m{}\33[m pessoas MAIORES de \33[31midade\33[m \n'
      'Houveram \33[31m{}\33[m pessoas MENORES de \33[31midade\33[m'.format(mr, mn))
