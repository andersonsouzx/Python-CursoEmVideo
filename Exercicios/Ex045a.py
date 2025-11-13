''' Crie um programa que faça o computador jogar JOKENPÔ com você.'''

import time
import random

itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
user  = int(input('Qual é a sua jogada? '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-='*13)
print(f'O computador jogou {itens[pc]}')
print(f'Você jogou {itens[user]}')
print('-='*13)

if pc == 0: # computador jogou PEDRA
    if user == 0:
        print('EMPATE')
    elif user == 1:
        print('JOGADOR VENCE')
    elif user == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1: # computador jogou PAPEL
    if user == 0:
        print('COMPUTADOR VENCE')
    elif user == 1:
        print('EMPATE')
    elif user == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2: # computador jogou TESOURA
    if user == 0:
        print('JOGADOR VENCE')
    elif user == 1:
        print('COMPUTADOR GANHA')
    elif user == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')