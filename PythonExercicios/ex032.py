'''32 Faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO
REGRA DO BISSEXTO:
De 4 em 4 anos é ano bissexto.
De 100 em 100 anos não é ano bissexto.
De 400 em 400 anos é ano bissexto.
Prevalecem as últimas regras sobre as primeiras.
'''
import string
from datetime import date
ano = int(input('Digite o ano: '))
c = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if ano == 0:
    ano = date.today().year
if c:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
