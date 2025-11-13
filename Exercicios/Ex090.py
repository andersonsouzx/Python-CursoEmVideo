# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário (se média >= 7, aprovado, se não, reporvado.). No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5: # ou elif 5 <= aluno['média'] < 7: (se m está entre 5 e 7)
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 20)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')