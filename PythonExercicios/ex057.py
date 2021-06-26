'''
57 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é seu gênero? \n'
                          '[M] Masculino\n'
                          '[F] Feminino\n'
                          'Digite sua escolha: ')).upper()
    if sexo == 'M':
        print('Seu gênero é \33[34mMasculino\33[m')
    if sexo == 'F':
        print('Seu gênero e \33[31mFeminino\33[m')
    if sexo != 'M' and sexo != 'F':
        print('-=-' * 10)
        print('\33[31mOpção inválida digite novamente!\33[m')
print('-=-' * 10)