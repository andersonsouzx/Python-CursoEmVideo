''' Desenvolva um programa que leia as duas notas de um aluno,
calcula e mostre sua média  '''

n1 = float(input('\033[96mDigite a primeira nota: \033[m'))
n2 = float(input('\033[96mDigite a segunda nota: \033[m'))
media = (n1 + n2) / 2

print(f'A média desse aluno foi: \033[33m{media:.1f}\033[m')