'''Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
 usando os comandos if.. elif.. else em programas Python.'''
#apenas if condição simples
#if + else condição composta
#if + elif + else condiçional alinhada(ninho)
nome = str(input('Qual e seu nome? '))
if nome == 'Jonathan':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'Matheus':
    print('Seu nome é bem popular')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e normal')
print('Tenha um bom dia {}'.format(nome))