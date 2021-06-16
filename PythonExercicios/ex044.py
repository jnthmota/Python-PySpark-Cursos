'''
44 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''
p = float(input('Valor do produto: R$ '))
f = int(input('Forma de pagamento: \n'
              '1 - À vista/cheque - desconto de 10%\n'
              '2 - À vista no cartão - desconto de 5%\n'
              '3 - Em até 2x no cartão - Preço normal\n'
              '4 - Em até 3x ou mais no cartão - Acrescimo de 20% de Juros\n'
              'Escolha sua forma de pagamento: '))
print('-=-' * 20)
print('Preço do produto R${}'.format(p))
if f == 1:
    regra = (p / 100) * 90
    print('Valor do produto com 10% de desconto ficará R${}'.format(regra))
elif f == 2:
    regra = (p/ 100) * 95
    print('Preço do produto com 5% de desconto R${}'.format(regra))
elif f == 3:
    print('Preço do produto em 2x no cartão R${}'.format(p))
elif f == 4:
    parcela = int(input('Quantas parcelas você deseja? '))
    regra = (p / 100) * 120
    x = (regra / parcela)
    print('Preço do produto ficou em {}x de R$:{} \n'
          'Valor total de R$:{} com 20% de juros'.format(parcela, x, regra))
else:
    print('-=-' * 20)
    print('Opção inválida, digite: \n'
          '1 - À vista/cheque - desconto de 10%\n'
          '2 - À vista no cartão - desconto de 5%\n'
          '3 - Em até 2x no cartão - Preço normal\n'
          '4 - Em até 3x ou mais no cartão - Acrescimo de 20% de Juros')
