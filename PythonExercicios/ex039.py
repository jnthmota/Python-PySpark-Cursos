'''
39 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que possou do prazo.
'''
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
s = int(input('Qual é seu Sexo?\n'
              '1 - M\n'
              '2 - F\n'
              'Digite sua escolha: '))
atual = date.today().year
idade = atual - ano
if idade == 18 and s == 1:
    print('Você tem que se alistar!!')
elif idade < 18 and s == 1:
    f = 18 - idade
    y = atual + f
    print('Você ainda não tem 18 anos, faltam {} anos para seu alistamento!'.format(f))
    print('Seu alistamento será no ano de {}'.format(y))
elif idade > 18 and s == 1:
    f = idade - 18
    y = atual - f
    print('Você está com {} anos! \n'
          'Você deveria ter se alistado há {} anos!'.format(idade, f))
    print('Seu alistamento foi no ano de {}'.format(y))
elif s == 2:
    print('No Brasil o alistamento militar é obrigatório apenas para o sexo masculino!')
else:
    print('-=-'* 20)
    print('Opção inválida! Digite [1] para Masculino ou [2] Feminino')
