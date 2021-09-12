'''
62 Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
con = 1
t = 0
continua = 10
while continua != 0:
    t = t + continua
    while con <= t:
        print('{} \33[31m ==> \33[33m'.format(termo), end='')
        termo += r
        con += 1
    print('\33[31m # PAUSA #\33[33m')
    continua = int(input('Quer adicionar quantos termos a mais? [Digite 0 para sair]'))
print('\33[31m#' * 7)
print('# FIM #')
print('#' * 7)