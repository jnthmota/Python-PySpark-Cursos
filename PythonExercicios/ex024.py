'''24 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não o nome "SANTO"'''
ci = str(input('Digite um nome de uma cidade: ')).strip()
print(ci[:5].lower() == 'santo')