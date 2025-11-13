''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE SE ALISTAR.
- Se ele já PASSOU DO TEMPO do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')

if idade < 18:
    ano_alistamento = nasc + 18
    print(f'Você deverá se alistar em {18 - idade} anos')
    print(f'Você ira se alistar no ano de {ano_alistamento}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    ano_alistamento = nasc + 18
    print(f'Você deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {ano_alistamento}')