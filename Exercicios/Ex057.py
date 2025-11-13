# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while not sexo or sexo not in 'MF': #ver se a entrada não é vazia e se é 'M' ou 'F'
    sexo = str(input('Erro, digite seu sexo novamente [M/F]: ')).strip().upper()[0]

if sexo == 'F':
    sexo = 'feminino'
else:
    sexo = 'masculino'

print(f'Sexo {sexo} registrado com sucesso!')