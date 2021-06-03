#tipos primitivos INT, FLOAT, BOOL, STR

#INT = (7, -4, 0, 9875)

#FLOAT (4.5, 0.076, -15.223, 7.0)

# BOOL (True, False)

# STR (String,  'Ola', '7,5', '')

n1 = int(input('primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
#print('A soma entre', n1,'e', n2,'vale', s) MODO ANTIGO
#print('A soma dos valores é {}'.format(s)) "NOVO MODELO"
print('A soma entre {} e {} vale {}'.format(n1, n2, s))


