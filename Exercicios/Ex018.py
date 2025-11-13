'''Faça um programa que leia um ângulo qualquer e mostre na tela 
 o valor do seno, cosseno e tangente desse ângulo.'''

import math

ang = float(input('Digite um ângulo qualquer: '))
ang_rad = math.radians(ang)

sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tan = math.tan(ang_rad)

print(f'O seno de {ang} é {sen:.2f}')
print(f'O cosseno de {ang} é {cos:.2f}')
print(f'A tangente de {ang} é {tan:.2f}')