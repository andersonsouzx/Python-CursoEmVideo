''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todos as mulheres.
D) Uma lista com todas as pessoas com idade acima da média. '''

pessoas = []
pessoa_dados = {}
soma = media = 0

while True:
    pessoa_dados['nome'] = input('Nome: ')
    pessoa_dados['sexo'] = input('Sexo [M/F]: ').strip().upper()[0] #apenas a 1° letra
    while pessoa_dados['sexo'] not in ['M', 'F']:
        pessoa_dados['sexo'] = input('Erro! digite apenas M ou F. ').strip().upper()
    pessoa_dados['idade'] = int(input('Idade: '))
    soma += pessoa_dados['idade']
    pessoas.append(pessoa_dados.copy())

    opc = input('Quer continuar [S/N]? ').strip().upper()[0]
    while opc not in ['S', 'N']:
        opc = input('Erro! responda apenas S ou N. ').strip().upper()
    if opc == 'N':
        break

print('-=' * 30)
print(f'A) O grupo tem {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) a média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p['nome']}, ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('    ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')