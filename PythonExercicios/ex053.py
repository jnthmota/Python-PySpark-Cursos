'''
53 Crie um programa que leia a frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
#palíndromo frase que pode ser lida de trás para frente
ex: APOS A SOPA => APOS A SOPA Polindromo (true)
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = '' #j[::-1] SEM FOR
for c in range(len(j) -1, -1, -1):
    i += j[c]
if i == j:
    print('PALÍNDROMO')
    print('Inverso de \33[31m{}\33[m ficou \33[31m{}\33[m'.format(f, i))
else:
    print('Frase não é um PALÍNDROMO')
print('-=-' * 10)