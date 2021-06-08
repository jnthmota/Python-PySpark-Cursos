#4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
n = input('Digite Algo: ') # n = OBJETO
r = n.istitle()
print('O tipo primitivo desse valor é', type(n)) # TYPE MOSTRA O TIPO
print('Tem espaço?  ', n.isspace()) #isspace() Método
print('É um número?  ', n.isnumeric())
print('É alfabético?  ', n.isalpha())
print('É alfanúmerico?  ', n.isalnum())
print('Está em maiúsculas?  ', n.isupper())
print('Está em minúsculas?  ', n.islower())
print('Está capitalizada? {}'.format(r)) # NOVO MODELO PYTHON3

