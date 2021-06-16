'''
43 Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e mostre seu status,
de acordo coma tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
p = float(input('Digite seu peso: KG '))
a = float(input('Digite sua altura: M '))
altura = a * a
imc = p / altura
if imc < 18.5:
    print('-=-'*20)
    print('Seu IMC esta em {:.2f}\n'
          '"ABAIXO DO PESO"'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('-=-'*20)
    print('Seu IMC esta em {:.2f}\n'
          '"PESO IDEAL"'.format(imc))
elif imc > 25 and imc <= 30:
    print('-=-'*20)
    print('Seu IMC esta {:.2f}\n'
          '"SOBREPESO"'.format(imc))
elif imc > 30 and imc < 40:
    print('-=-'*20)
    print('Seu IMC esta {:.2f}\n'
          '"OBESIDADE'.format(imc))
else:
    print('-=-'*20)
    print('Seu IMC esta {:.2f}\n'
          '"OBESIDADE MÓRBIDA"'.format(imc))