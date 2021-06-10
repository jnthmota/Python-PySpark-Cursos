''' Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender
são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().   '''

frase = 'Curso em Video Python'
print(frase[::2])
print(frase.upper().count('O'))
print(len(frase))
print(frase.split())
divido = frase.split()
print(divido[2])
print('Curso' in frase)
print(frase.find('video'))
print(frase.lower().find('video'))
print(frase.replace('Python', 'Pyspark'))
frase = frase.replace('Python', 'Pyspark') # Uma string e imutavel, portanto tenho que fazer uma atribuição
print(frase)
print("""
P
R
I
N
T

T
U
D
O
""")
