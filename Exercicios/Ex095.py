# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
time = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    gols = []
    for g in range(partidas):
        gols.append(int(input(f'   Quantos gols na partida {g+1}? ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    opc = input('Quer continuar? [S/N] ').strip().upper()[0]
    while opc not in ['S', 'N']:
        opc = input('Erro. Digite apenas S ou N ').strip().upper()[0]

    time.append(jogador.copy())

    if opc == 'N':
        break

print('-=' * 25)

print('cód ', end='')
for e in jogador.keys(): # exibindo cada elemento(cod, gols, total) de jogador
    print(f'{e:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values(): # Lê-se: para cada dado em v
        print(f'{str(d):<15}', end='')
    print()

print('-' * 50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}')
        for i, g in enumerate(time[busca]['gols']): #mostrando o num de gols do jog.
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 50)

print('<<< VOLTE SEMPRE >>>')