'''
52 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
nr = int(input('Digite um número: '))
con = 0
for c in range(1, nr + 1):
    if nr % c == 0:
        print('\33[31m', end='')
        con += 1
    else:
        print('\33[m', end='')
    print('{}\33[m'.format(c))

print('O número \33[33m{}\33[m foi divido \33[31m{}x\33[m'.format(nr, con))
if con == 2:
    print('Número é \33[31mPRIMO\33[m')
else:
    print('\33[31mNão\33[m é PRIMO')
print('-=-' * 10)
