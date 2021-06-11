'''Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos
seus programas em Python.'''

'''
carro.siga()
 if carro.esquerda():
     carro.siga()
     carro.direita()
     carro.siga()
     carro.direita()
     carro.esquerda()
     carro.siga()
     carro.direita()
     carro.siga()
  else:
      carro.siga()
      carro.esquerda()
      carro.siga()
      carro.esquerda()
      carro.siga
  carro.break()'''

tempo = int(input('Quanto anos tem seu carro? '))
if tempo <=3:
    print('Seu carro ta novo')
else:
    print('Seu carro ta na hora de trocar')
print('-'*40)

#Modo simplificado
tempo = int(input('Quanto anos tem seu carro?' ))
print('Seu carro ta novo'if tempo<=3 else 'Seu carro ta na hora de trocar')
print('-'*40)