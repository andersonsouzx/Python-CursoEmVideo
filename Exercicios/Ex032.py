''' Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO. '''

ano = int(input('Digite um ano qualquer: '))

if ano % 400 == 0:
    print('Bissexto.')
elif ano % 100 == 0:
    print('Não bissexto.')
elif ano % 4 == 0:
    print('Bissexto.')
else:
    print('Não bissexto.')