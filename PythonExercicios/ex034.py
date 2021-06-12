'''34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para salários inferiores ou iguais,o aumento e de 15%'''
sl = float(input('Qual é seu salário? '))
a = (sl / 100) * 110
a1 = (sl / 100) * 115
if sl > 1250:
    print('Seu salário teve um reajuste de 10%, ficou em R${}, Parabéns!'.format(a))
else:
    print('Seu salário teve um reajuste de 15%, ficou em R${}, Parabéns!'.format(a1))