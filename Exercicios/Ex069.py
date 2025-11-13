''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá peruntar se o usuário quer ou não continuar. No final, mostre:


A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.   '''

print('CADASTRO DE PESSOAS')

maior18 = 0
homenscad = 0
mulhermenor18 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-' * 30)
    idade = int(input('Idade: '))

    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0] # ou sexo = ''
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)

    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0] # ou opcao = ''
    while opcao not in ['S', 'N']:
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if idade >= 18:
        maior18 += 1

    if sexo == 'M':
        homenscad += 1

    if (sexo == 'F') and idade < 20:
        mulhermenor18 += 1
    
    if opcao == 'N':
        print('\n====== FIM DO PROGRAMA ======')
        break

print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo temos {homenscad} homens cadastrados.')
print(f'E temos {mulhermenor18} mulheres com menos de 20 anos.')