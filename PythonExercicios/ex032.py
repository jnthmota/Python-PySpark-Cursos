'''32 Faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO'''
ano = int(input('Digite o ano: '))
c = ano % 4
if c == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
