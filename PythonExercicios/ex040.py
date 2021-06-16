'''
40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO
'''
a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = (a + b) / 2
if c < 5.0:
    print('-=-'*20)
    print('Sua média foi de {} \n'
          'REPROVADO! Se dedique mais.'.format(c))
elif c > 5.0 and c <= 6.9:
    print('-=-'*20)
    print('Sua média foi de {} \n'
          'RECUPERAÇÃO! Estude mais.'.format(c))
else:
    print('-=-'*20)
    print('Sua média foi de {} \n'
          'APROVADO! Parabéns ...'.format(c))