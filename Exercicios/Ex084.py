''' Faça um programa que leia o nome e peso de vária pessoas, guardando tudo em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.  '''

dados = []
pessoas = []
maior_peso = menor_peso = 0
pessoa_maior_peso = []
pessoa_menor_peso = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = input('Quer continuar? [S/N] ').strip().upper()
    while resp not in ['S', 'N']:
        resp = input('Erro. Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-=' * 20)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
for p in pessoas:
    if p[1] == maior_peso:
        pessoa_maior_peso.append(p[0])
    if p[1] == menor_peso:
        pessoa_menor_peso.append(p[0])
print(f'O maior peso foi de {maior_peso}Kg. peso de {pessoa_maior_peso}')
print(f'O menor peso foi de {menor_peso}Kg. peso de {pessoa_menor_peso}')