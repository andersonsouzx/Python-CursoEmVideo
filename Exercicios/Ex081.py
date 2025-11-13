''' Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.    '''

num = []

while True:
    num.append(int(input('Digite um valor: ')))

    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()
    while opcao not in ['S', 'N']:
        opcao = str(input('Erro. Digite apenas: [S/N]? ')).strip().upper()
    if opcao == 'N':
        break

print('-=' * 20)
print(f'Você digitou {len(num)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(num, reverse=True)}')
print(f'O valor 5 faz parte da lista!' if 5 in num else 'O valor 5 não foi encontrado na lista!')