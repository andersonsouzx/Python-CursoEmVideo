''' Faça um programa que leia um número qualquer e mostre o seu FATORIAL.

Ex:
5!= 5x4x3x2x1= 120  '''

num = int(input('Digite um número para calcular seu Fatorial: '))
count = num
factor = 1

print(f'Calculando {num}! = ', end='')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    factor *= count
    count -= 1 # count= count - 1
print(f'{factor}')


# -----------------------------------------------------------------------------
#usando for e biblioteca math
'''from math import factorial
n = int(input('Digite um número: '))

print(f'Calculando {n}! = ', end='')
for i in range(n, 0, -1):
    print(f'{i}', end='')
    print('x' if i > 1 else ' = ', end='')
print(factorial(n))'''