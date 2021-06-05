#06)CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

a = int(input('Digite um valor: '))
d = a * 2
t = a * 3
rq = a ** (1/2)
print('O seu dobro de {} é: {} \n O seu triplo de {} é: {} \n A  raiz Quadrada de {} é: {:.4}'.format(a, d, a, t, a, rq))