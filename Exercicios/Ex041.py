''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER     '''

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if ano > ano_atual:
    print('Ano de nascimento inválido. Tente novamente!')
else:
    print(f'O atleta tem {idade} anos.')
    if idade <= 9:
        print('Classificação: MIRIM')
    elif idade <= 14:
        print('Classificação: INFANTIL')
    elif idade <= 19:
        print('Classificação: JUNIOR')
    elif idade <= 25:
        print('Classificação: SÊNIOR')
    else:
        print('Classificação: MASTER')