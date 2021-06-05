#05)FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

n = int(input('Digite um valor: '))
a = n - 1
s = n + 2
print('Valor Digitado: {:^3} \n Seu antecessor: {} \n Seu sucessor: {:^5}'.format(n, a, s))