'''
49 Refaça o DESAFIO 009, mostrando a tabuada de um número que o usúario escolher, só que agora
utilizando um laço for.
'''
tabuada = int(input('Tabuada: '))
print('-=-' * 10)
for t in range(1, 11):
    r = tabuada * t
    print('{}x{} = {}'.format(tabuada, t, r))
print('-=-' * 10)
