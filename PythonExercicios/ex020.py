'''' 20 O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno : '))
d = str(input('Quarto aluno: '))
list = [a, b, c, d]
random.shuffle(list)
print('A ordem para apresentação é: {}'.format(list), end=' ')