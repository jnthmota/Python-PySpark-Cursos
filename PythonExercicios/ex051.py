'''
51 Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(p, 11, r):
    print('{}'.format(c))
print('-=-' * 10)
