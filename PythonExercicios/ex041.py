'''
41 A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos, portanto sua categoria é: \n'
          'MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos, portanto sua categoria é: \n'
          'INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos, portanto sua categoria é: \n'
          'JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos, portanto sua categoria é: \n'
          'SENIOR')
else:
    print('Você tem {} anos, portanto sua categoria é: \n'
          'MASTER'.format(idade))