# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

trabalhador = {}
 
trabalhador['nome'] = input('Nome: ')
ano_nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - ano_nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem ): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    contribuicao = date.today().year - trabalhador['contratação']
    anos_contribuicao = 35 - contribuicao
    trabalhador['aposentadoria'] = trabalhador['idade'] + anos_contribuicao
  # trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - date.today().year)  // uma forma mais minimalista

print('-=' * 25)
#print(trabalhador)

for k, v in trabalhador.items():
    print(f'  -- {k} tem valor {v}')