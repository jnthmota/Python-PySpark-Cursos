'''
48 Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''
s = 0
con = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        con +=  1
print('A soma entre todos os números impares é {} \n'
      'São múltiplos de três são {} '.format(s, con))
