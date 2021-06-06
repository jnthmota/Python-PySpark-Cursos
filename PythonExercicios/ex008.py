#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMENTROS E MILIMETROS

v = float(input('Digite um valor em metros: '))
cm = v * 100
mm = v * 1000
print('A medida de {} metros convertida em \n cm é: {} \n mm é: {}'.format(v, cm, mm))
