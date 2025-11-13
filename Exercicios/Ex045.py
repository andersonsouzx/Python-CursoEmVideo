''' Crie um programa que faça o computador jogar JOKENPÔ com você.'''

import time
import random

opcoes = ['Pedra', 'Papel', 'Tesoura']

user = input('Escolha: Pedra, Papel ou Tesoura? ').capitalize()
pc = random.choice(opcoes)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print(f'Você escolheu: {user}')
print(f'O computador escolheu: {pc}')

if user == pc:
    print('Empate!')
elif (user == 'Pedra' and pc == 'Tesoura') or \
    (user == 'Tesoura' and pc == 'Papel') or \
    user == 'Papel' and pc == 'Pedra':
    print('Você ganhou!')
else:
    print('Você perdeu.')