#14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
t = float(input('Digita a temperatura em ºC: '))
f = ((9 * t) / 5) + 32
print('Temperatura de {}ºC é {}ºF'.format(t, f))