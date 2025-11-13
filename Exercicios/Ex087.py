''' Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha.  '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = socol = mail = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{[matriz[l][c]]}', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

print('-=' * 25)
print(f'A soma dos valores pares é {spar}.')

for l in range(0, 3):
    socol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {socol}.')

for c in range(0, 3):
    if c == 0 or matriz[1][c] > mail:
        mail = matriz[1][c]
'''for c in range(0, 3):
    if c == 0 or matriz[1][c] > mail:
        mail = matriz[1][c]
    if matriz[1][c] > mail:
        mail = matriz[1][c]'''

print(f'O maior valor da segunda coluna é {mail}.')