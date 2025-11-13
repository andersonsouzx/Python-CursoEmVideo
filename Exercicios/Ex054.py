# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

menores = 0
maiores = 0

for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - ano
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f'\nHá {menores} pessoas que não atingiram sua maioridade.')
print(f'Há {maiores} pessoas que já são maiores de idade.')