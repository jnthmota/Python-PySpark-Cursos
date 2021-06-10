''' Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender
são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().   '''

frase = 'Curso em Video Python'
frase = [9] #Vai pega a nona letra da lista
frase = [9:13] = #Vai pega o intervalo de 9:13 que seria 'Vide' fatiamento sempre pega um a menos
frase = [9:21] = # Vai pega o intervalo de 9:21 'Video Python'
frase = [9:21:2] = # Vai pega o intervalo de 9:21 porem saltando de 2 em 2 = 'Vdo Pto'
frase = [:5] = # Vai pega os 5 primeiros do fatiamento = 'Curso'
frase = [15:] = # Vai pega de os ultimos carateres da fatima do 15 ate o ultimo = 'Python'
frase = [9::3] =  #Vai começa no 9:: e vai ate o final 'Video Python', :3 vai pular em 3 , = 'Ve Ph'

#Analise

len(frase) # Qual o comprimento da frase? len de frase seria 21 Caracteres
frase.count('o') # Contar quantas vezes aparece a letra 'o'(minuscula) case sensitive da frase = 3
frase.count('o',0,13) # Contagem com fatiamento vai considerar do 0 até o 13 = apenas 1 'o'
frase.find('deo') # Quantas vezes ele encontrou a frase 'deo' = [11]
frase.find('Android') # Vai te retornar um -1 então significa que essa palavra não foi encontrada na lista
'Curso' in frase # Existe curso em frase ? se houver será {True}


#Transformação

frase.replace('Python','Android') # Vai substituir Python por Android
frase.upper() # METODO UPPER, VAI FICAR TUDO MAIUSCULO
frase.lower() # METODO LOWER, vai fica tudo minusculo
frase.capitalize() #METODO CAPITALIZE, vai joga toda a frase minuscula, porém a primeira letra Maiuscula
frase.title() # METODO TITLE, vai fazer uma analise mais profunda, verificar onde tem uma quebra de espaço e o
#primeiro caracter e transformar em maiusculo
frase.strip() # METODO STRIP, remove os espaços inuteis no começo e no final
frase.rstrip() # METEDO STRIP, vai tratar o lado direto da string, ou seja so o final
frase.lstrip()# METEDO STRIP, vai tratar o lado esquerda da string, ou seja so o começo

# Divisão

frase.split() # METODO SPLIT, vai ocorrer uma divisão entre os espaços da frase, uma nova indexão
# [Curso] [em] [Video] [Python] 0-3 lista

#Junção

'-'.join(frase) # Juntar todos os elementos e vai usar '-' como separador = Curso-em-Video-Python