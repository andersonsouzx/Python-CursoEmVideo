''' Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário 
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na ela se o usuário venceu ou perdeu. '''

import random
from time import sleep

print('-=-' * 25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numpc = random.randint(0, 5)
print('-=-' * 25)
numuser = int(input('Em que número eu pensei?  '))
print('Processando...')
sleep(3) #método para adicionar um time

if numpc == numuser:
    print(f'Parabéns, você ganhou!')
else:
    print(f'Você perdeu, o número escolhido foi: {numpc}')