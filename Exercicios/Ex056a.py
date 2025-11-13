'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

* A MÉDIA DE IDADE do grupo.
* Qual é o nome do homem mais velho.
* Quantas mulheres têm menos de 20 anos.    '''

somaidd = 0
midade = 0
validos = 0
idd_maisvelho = 0
nome_velho = ''
mulhers20 = 0

for i in range(1, 5):
    print(f'----- {i}ª pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo not in 'MmFf':
        print('Sexo inválido, os dados desse usuário será ignorado!')
        continue

    somaidd += idade
    validos += 1

    if i == 1 and sexo in 'Mm':
        idd_maisvelho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > idd_maisvelho:
        idd_maisvelho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulhers20 += 1

if validos > 0:
    midade = somaidd / validos
    print(f'A média de idade do grupo é de {midade} anos.')
else:
    print('Não há dados válidos para calcular a média.')

print(f'O home mais velho se chama {nome_velho} e tem {idd_maisvelho} anos.')
print(f'Há {mulhers20} mulheres com menos de 20 anos.')