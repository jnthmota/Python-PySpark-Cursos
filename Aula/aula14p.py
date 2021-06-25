'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição
while no Python
'''
'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''
# exemplo sem limite
n = 1
while n != 0: # Condição de parada
    n = int(input('Digite um valor: '))
print('Fim')

# exemplo 2
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

# exemplo 3
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} PARES e {} IMPARES'.format(par, impar))

