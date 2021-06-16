'''
38 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. os dois são iguais
'''
nr = int(input('Digite o primeiro número: '))
nr1 = int(input('Digite o segundo número:  '))
if nr > nr1:
    print('-=-'*20)
    print('O valor {} é MAIOR que {}'.format(nr, nr1))
elif nr1 > nr:
    print('-=-'*20)
    print('O valor {} é MAIOR que {}'.format(nr1, nr))
elif nr == nr1:
    print('-=-'*20)
    print('Não existe valor MAIOR \n'
          'O primeiro valor "{}" é igual ao segundo valor "{}"'.format(nr, nr1))
    print('-=-'*20)