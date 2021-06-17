'''
Aula 13 – Estrutura de repetição for
Repetições em Python (for)
'''
for c in range(0, 6):
    print('Oi')
print('FIM')

for c in range(6, 0, -1): #contar para trás
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')

#================================
i = int(input('Inicio:  '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

#====================================
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('fim')

#=========================
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))