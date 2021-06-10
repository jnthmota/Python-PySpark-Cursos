''' Um Professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
 lendo o nome deles e escrevendo o nome do escolhido.'''
import random
a = str(input('Primeiro Aluno: '))
b = str(input('Segundo Aluno: '))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto Aluno: '))
lis = [a, b, c, d]
r = random.choice(lis)
print('O aluno escolhido foi: {} '.format(r))
