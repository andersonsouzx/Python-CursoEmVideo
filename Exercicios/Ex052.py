# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=" ")
        total += 1
    else:
        print('\033[31m', end=" ")
    print(f'{i}', end=' ' '\033[m')
print(f'\n\nO número {num} foi dividido {total} vezes')
print('E por isso ele É PRIMO!' if total == 2 else 'E por isso ele É COMPOSTO!')



'''num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=" ")
        total += 1
    else:
        print('\033[31m', end=" ")
    print(f'{i}', end=' ' '\033[m')
print(f'\n\nO número {num} foi dividido {total} vezes')
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele É COMPOSTO!') # número não primo
'''