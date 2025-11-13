''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas '''

allnum = []
numpar = []
numimpar = []

while True:
    allnum.append(int(input('Digite um valor: ')))

    opcao = input('Quer continuar [S/N]? ').strip().upper()
    while opcao not in ['S', 'N']:
        opcao = input('Erro, digite apenas [S ou N]: ').strip().upper()
    if opcao == 'N':
        break

for v in allnum:
    numpar.append(v) if v % 2 == 0 else numimpar.append(v)

print('-=' * 25)
print(f'A lista completa é {allnum}')
print(f'A lista de pares é {numpar}')
print(f'A lista de impares é {numimpar}')