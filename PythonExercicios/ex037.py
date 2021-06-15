'''
37 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
from time import sleep
n = int(input('Digite qualquer número inteiro: '))
p = int(input('Qual base de conversão você deseja? \n'
              '1 - Binário\n'
              '2 - Octal\n'
              '3 - Hexadecimal\n'
              'Digite sua escolha: '))
binary = bin(n)
octal = oct(n)
hexadecimal = hex(n)
print('-=-'*20)
print('CONVERTANDO ... ')
sleep(4)
if p == 1:
    print('O número digitado {} convertido para Binário ficou:\n'
          '{}'.format(n, binary))
elif p == 2:
    print('O número digitado {} convertido para Octal ficou:\n'
          '{}'.format(n, octal))
elif p == 3:
    print('O número digitado {} convertido para Hexadecimal ficou:\n'
          '{}'.format(n, hexadecimal))
else:
    print('Opção inválida, tente novamente digitando entre [1][2][3]')