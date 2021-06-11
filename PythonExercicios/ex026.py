'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''
p = str(input('Digite alguma frase: ')).strip()
print('Letra "A" aparece {} vezes em sua digitação '.format(p.upper().count('A')))
print('Ela aparece pela primeira vez na posição {} '.format(p.upper().find('A')))
print('Ela aparece pela última vez na posição {}'.format(p.upper().rfind('A')))