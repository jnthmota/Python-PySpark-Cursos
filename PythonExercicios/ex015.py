#15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por Km rodado.
c = int(input('Qual foi a quantidade de KM percorrido? '))
d = int(input('Alugou por quantos dias? '))
p = d * 60 + c * 0.15
print('Você alugou o carro por {} dias e percorreu {}KM'.format(d, c))
print('=' * 50)
print('Valor total a ser pago e de R$: {:.2f} '.format(p))