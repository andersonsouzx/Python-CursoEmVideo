''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol de 2025, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time do Fluminense    '''

times_brasileirao_2024 =(
    'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
    'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
    'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
    'RB Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print('-=' * 15)
print(f'Lista de times do Brasileirão 2024: {times_brasileirao_2024}')
print('-=' * 15)
print(f'Os cinco primeiros são {times_brasileirao_2024[:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {times_brasileirao_2024[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {tuple(sorted(times_brasileirao_2024))}')
print('-=' * 15)
print(f'O Fluminense está na {times_brasileirao_2024.index('Fluminense') + 1}ª posição')