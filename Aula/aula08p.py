#Aula prática
import math #tudo
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz do {} é igual a {:.2f}'.format(n,raiz))

# Arredondando para cima
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz do {} é igual a {}'.format(n, math.ceil(raiz)))

# Arredondando para baixo
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz do {} é igual a {}'.format(n, math.floor(raiz)))

# =======================================================

from math import sqrt,floor #Importa somente o sqrt e floor

n = int(input('Digite um número: '))
raiz = sqrt(n)
print('A raiz do {} é igual a {:.2f}'.format(n,raiz))

# Arredondando para cima
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz do {} é igual a {}'.format(n, floor(raiz)))

# =======================================================

import random

n = random.random()
print(n)

n = random.randint(1, 10) #numero inteiro
print(n)

# =======================================================

import emoji
print(emoji.emojize('Ola mundo :sunglasses: ', use_aliases=True))