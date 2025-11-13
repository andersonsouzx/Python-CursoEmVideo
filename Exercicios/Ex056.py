'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

* A MÉDIA DE IDADE do grupo.
* Qual é o nome do homem mais velho.
* Quantas mulheres têm menos de 20 anos.    '''

somaidd = 0
mais_velho = 0
nome_velho = ''
mulheres20 = 0

for i in range(1, 5):
    print(f'----- {i}ª pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    somaidd += idade

    if i == 1 and sexo in 'Mm' :
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > mais_velho:
            mais_velho = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
              mulheres20 += 1

midade = somaidd / 4

print(f'\nA média de idade do grupo é de {midade} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulheres20} mulheres com menos de 20 anos.')