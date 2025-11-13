''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE SE ALISTAR.
- Se ele já PASSOU DO TEMPO do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date

sexo = str(input('Informe seu sexo (M/F): ')).strip().upper() #tirando possiveis espacos e colocando tudo em maiusculo.

if sexo == 'F':
    print('O alistamento obrigatório é somente para homens!')
elif sexo == 'M':
    print('\nBem vindo ao alistamento militar obrigatório!'.upper())
    nasc = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} em {ano_atual}.\n')

    if idade < 18:
        ano_alistamento = nasc + 18
        print(f'Você irá se alistar em {18 - idade} anos.')
        print(f'Você irá se alistar no ano de {ano_alistamento}')
    elif idade == 18:
        print('Você deve se alistar \033[33mIMEDIATAMENTE!\033[m')
    else:
        ano_alistamento = nasc + 18
        print(f'Você deveria ter se alistado há {idade - 18} anos.')
        print(f'Seu alistamento foi em {ano_alistamento}.')
        print('\033[31mJÁ PASSOU DA HORA DE SE ALISTAR RECRUTA!\033[m')
else:
    print('Opção inválida!')