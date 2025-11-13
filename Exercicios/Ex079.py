# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crecente

numembers = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in numembers:
        print('Valor duplicado! Não irei adicionar...')
    else:
        numembers.append(valor)
        print('Valor adicionado com sucesso...')

    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()
    if opcao not in ['S', 'N']:
        print('Erro. Tente novamente...')
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()

    if opcao == 'N':
        break

print('-=' * 20)
#numembers.sort()
#print(f'Você digitou os valores {sorted(numembers)}')
print(f'Você digitou os valores {', '.join(map(str, sorted(numembers)))}')