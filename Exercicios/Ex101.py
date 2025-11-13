# Crie um programa que tenha uma função chamada vota() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem idade NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

print('-' * 20)

def vota(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif idade >= 16 and idade < 18 or idade >= 60:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')

vota(int(input('Em que ano você nasceu? ')))

'''
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 60:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
'''