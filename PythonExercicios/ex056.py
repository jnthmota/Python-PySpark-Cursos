'''
56 Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 21 anos.
'''
sidade = 0 # soma idade
midade = 0 #media
mridade = 0 #maior idade
nvelho = 0 # nome velho
qtmulher = 0 # quantidade de mulheres
for c in range(1, 5):
    print('-=-' * 10)
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Idade: '))
    sexo = int(input('Qual seu sexo?\n'
                  '1 - \33[34mM\33[m\n'
                  '2 - \33[31mF\33[m\n'
                  'Digite uma opção: '))
    sidade += idade
    if c == 1 and sexo == 1:
        mridade = idade
        nvelho = nome
    if sexo == 1 and idade > mridade:
        mridade = idade
        nvelho = nome
    if sexo == 2 and idade > 20:
        qtmulher += 1
midade = sidade / 4
print('A média de idade do grupo é \33[31m{}\33[m\n'
      'O nome do homem mais velho tem \33[34m{}\33[m é se chama \33[34m{}\33[m\n'
      'Existe \33[31m{}\33[m mulheres que tem menos de 20 anos'.format(midade, mridade, nvelho, qtmulher))
