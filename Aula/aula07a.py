# EXEMPLO DE STRING

print('Oi' + 'Ola')
# STRING + INT
print('Oi' * 5)
print('='*30)

# OPERADORES REPLICANDO INFORMAçÃO (STRING)

nome = input('Qual é seu nome??')
print('Prazer em te conhecer {:20}'.format(nome))
print('Prazer em te conhecer {:>20}'.format(nome))
print('Prazer em te conhecer {:<20}'.format(nome))
print('Prazer em te conhecer {:^20}'.format(nome)) # CENTRALIZADO em 20 espaços
print('Prazer em te conhecer {:=^20}'.format(nome)) # CENTRALIZADO em 20 espaços com iguais em volta


# OPERADORES

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor'))
print('A soma vale {}'.format(n1+n2))

# OTIMIZANDO

n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A Soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') # .3 CASAS A DIREITA f FLUTUANDO
#END continua o print na mesma linha
#\n quebra linha
print('A divisão inteira {} e potência {}'.format(di, e))
