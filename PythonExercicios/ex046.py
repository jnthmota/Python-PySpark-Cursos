'''
46 Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio,
indo de 10 até 0, com uma pause de 1 segundo entre eles.
'''
import emoji
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize("BOOOOOMMM :fireworks::fireworks::fireworks::fireworks:"))