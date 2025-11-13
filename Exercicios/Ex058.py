# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

count = 1

print('Irei pensar em um número, tente adivinhar!')
print('-=-' * 15)
numpc = random.randint(0, 10)
numuser = int(input('Em que número eu pensei?  '))
while numpc != numuser:
    if numpc < numuser:
        print('Mais baixo... Tente novamente!')
    else:
        print('Mais alto... Tente novamente!')
    numuser = int(input('Qual é seu novo palpite? '))
    count += 1

print('-=-' * 15)
print(f'Parábens, o número escolhido era {numpc}.')
print(f'Foram necessárias {count} tentativas para você acertar.')