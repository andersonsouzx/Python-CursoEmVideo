# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0

while True:
    n = int(input('Digite um número para ver sua tabuada: '))

    if n < 0:
        print('Número negativo. Finalizando o programa...')
        break

    print('-=' * 15)
    print(f'Tabuada do {n}')
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-=' * 15)

print('FIM.')