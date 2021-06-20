'''
50 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
PARES.
Se o valor digitado for ímpar,desconsidere-o.
'''
s = 0
for n in range(1, 7):
    a = int(input('Digite o {}° número: '.format(n)))
    if a % 2 == 0:
        s += a
print('-=-' * 20)
print('A soma dos números PARES ficou {}'.format(s))
