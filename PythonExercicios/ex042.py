'''
42 Refaça o DESAFIO 035 dos triângulos, acrescentado o recurso de mostrar que tipo de triângulo será
formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas digitadas podem formar um triângulo')
    print('-=-'* 20)
    if a == b == c:
        print('As retas formam um "EQUILÁTERO"')
    elif a != b != c != a:
        print('As retas foram um "ESCALENO"')
    else:
        print('As retas formam um "ISÓSCELES"')
else:
    print('As retas não pode FORMAR um triângulo!')

