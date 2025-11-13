# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostar as notas de cada aluno individualmente.

alunos = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ').strip().upper()
    while resp not in ['S', 'N']:
        resp = input('Erro. Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-=' * 15)
print(f'{'N°':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

while True:
    print('-' * 30)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    while (opc < 0 or opc > len(alunos) -1)  and opc != 999:
        opc = int(input('Opção inválida. tente novamente: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'As notas de {alunos[opc][0]} são {alunos[opc][1]}')
    else:
        print('Erro. Tente novamente.')
print('<<< VOLTE SEMPRE >>>')