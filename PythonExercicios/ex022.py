'''22 Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras ao td (sem considerar o espaços)
- Quantas letras tem o primeiro nome'''

n = str(input('Digite o nome completo: '))
div = n.split()
print('Nome com todas as letras maiusculas: {}'.format(n.upper()))
print('Nome com todas as letras minusculas: {}'.format(n.lower()))
print('Quantas letras ao todo: {}'.format(len(n) - n.count(' ')))
print('Seu nome {} tem {} letras no primeiro nome'.format(n, len(div[0])))
