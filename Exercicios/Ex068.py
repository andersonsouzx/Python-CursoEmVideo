# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 25)

count = 0

while True:
    numuser = int(input('Diga um valor: '))

    while True:
        parorimp = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
        if parorimp not in ['P', 'I']:
            print('Erro. Digite novamente!')
        else:
            break # verificando se o usuário digita corretamente P ou I

    numpc = randint(0, 10)
    soma = numuser + numpc

    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'

    print(f'Você jogou {numuser} e o computador {numpc}. Total de {soma} DEU {resultado}')

    if (parorimp == 'P' and resultado == 'PAR') or (parorimp == 'I' and resultado == 'ÍMPAR'):
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 25)
    else:
        print('Você PERDEU!')
        print('=-' * 25)
        break
    count += 1

print(f'GAME OVER! Você venceu {count} vezes.')