''' Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos g ele marcou.

    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.  '''

print('-' * 25)
def ficha(nome='<desconhecido>', gols=0):
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
g= input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0

if nome.strip() == '': #se o nome estiver vazio, irá passar apenas os g.
    ficha(gols= g) 
else:                  #caso contrário, passará o nome e os g para a função ficha
    ficha(nome, g)