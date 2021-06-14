'''Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
 usando os comandos if.. elif.. else em programas Python.'''

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
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
else:
    carro.siga()
carro.break()
