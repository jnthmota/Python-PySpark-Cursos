'''27 Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e o
último nome separadamente'''
nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('Seu primeiro nome é {} \nSeu último nome é {}'.format(div[0], div[len(div)-1]))
