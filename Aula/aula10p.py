'''Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos
seus programas em Python.'''
nome = str(input('Qual é seu nome? '))
if nome == 'Jonathan':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão comum')
    print('Bom dia, {}'.format(nome))

#----------------------------------------------------------------------------------------------------

n = float(input('Digite a primeira nota: '))
n1 = float(input('Digite a segunda nota: '))
n2 = (n + n1) / 2
if n2 >= 6.0:
    print('Sua média foi {:.2f}, isso e ótimo, parabens!'.format(n2))
else:
    print('Sua média foi {:.2f}, não foi boa, estude mais!'.format(n2))




