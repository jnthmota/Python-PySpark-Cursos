#05: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um valor: '))
a = n - 1
s = n + 2
print('Valor Digitado: {:^3} \n Seu antecessor: {} \n Seu sucessor: {:^5}'.format(n, a, s))