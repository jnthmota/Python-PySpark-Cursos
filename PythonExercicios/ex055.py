'''
55 Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o MAIOR e o MENOR peso lidos.
'''
mr = 0
mn = 0
for p in range(1, 6):
    peso = float(input('Qual é o peso da {}° pessoa? KG '.format(p)))
    if p == 1:
        mr = peso
        mn = peso
    else:
        if peso > mr:
            mr = peso
        if peso < mn:
            mn = peso
print('-=-' * 12)
print('O MAIOR PESO é: \33[31m{}\33[m\n'
      'O MENOR PESO é: \33[31m{}\33[m'.format(mr, mn))
print('-=-' * 12)
