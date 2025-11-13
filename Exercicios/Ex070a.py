''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário  vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.    '''

from time import sleep

print('-' * 30)
print('LOJA SUPER BARATÃO'.center(30))
print('-' * 30)

soma = maismil = count = menor = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('preço: R$ '))
    opcao = ''
    while opcao not in ['S', 'N']:
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    count += 1
    soma += preco
    if preco > 1.000:
        maismil += 1
    if count == 1 or preco < menor:
        menor = preco
        barato = produto
    if opcao == 'N':
        print('Finalizando sua compra...')
        sleep(3)
        break

print(f'\nTotal gasto: R${soma:.2f}')
print(f'{maismil} produtos custam mais de R$1.000,00')
print(f'O produto mais barato foi {barato}, custando R${menor:.2f}')