#08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

v = float(input('Digite um valor em metros: '))
cm = v * 100
mm = v * 1000
print('A medida de {} metros convertida em \n cm é: {} \n mm é: {}'.format(v, cm, mm))
