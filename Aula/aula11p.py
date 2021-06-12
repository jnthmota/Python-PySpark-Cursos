print('\33[31mTUDO COLORIDO')
print('\33[31;43mTUDO COLORIDO\33[m')
print('\33[1;31;43mTUDO COLORIDO\33[m')
print('\33[4;30;45mTUDO COLORIDO\33[m')
print('\33[30mTUDO COLORIDO\33[m')
print('\33[7;30mTUDO COLORIDO\33[m')
print('\33[0;30;44mTUDO COLORIDO\33[m')
print('\33[7;30;44mTUDO COLORIDO\33[m')
a = 3
b = 5
print('Os valores são \33[32m{}\33[m e \33[31m{}\33[m'.format(a, b))

#LISTA DE CORES DICIONARIO
COLORIDO = 'ARRASSOU'
cores = {'limpa': '\33[m',
         'azul': '\33[34m',
         'amarelo':'\33[33m',
         'pretoebranco':'\33[7;30m'}

print('COLOCANDO PARAMETRO NAS CORES {}{}{}'.format(cores['amarelo'], COLORIDO, cores['limpa']))
