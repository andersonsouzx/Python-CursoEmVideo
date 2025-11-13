''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário  vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.    '''

print('-' * 30)
print('LOJA SUPER BARATÃO'.center(30))
print('-' * 30)

soma = 0
pmaismil = 0
nomemaisbarato = []
pmaisbarato = []

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0] # opcao = ''
    while opcao not in ['S','N']:
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    
    soma += preco
    if preco > 1000:
        pmaismil += 1

    nomemaisbarato.append(nome)
    pmaisbarato.append(preco)

    if opcao == 'N':
        print('FIM DO PROGRAMA'.center('-'*30))
      # print('{:-^40}'.format(' FIM DO PROGRAMA '))
        break

print(f'\nO total de compra foi R${soma:.2f}')
print(f'Temos {pmaismil} custando mais de R$1.000,00')
print(f'O produto mais barato foi {min(nomemaisbarato)} que custa R${min(pmaisbarato):.2f}')