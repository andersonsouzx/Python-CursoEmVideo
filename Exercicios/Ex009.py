"""Faça um programa que leia um número inteiro qualquer
 e mostre na tela a sua tabuada"""

num = int(input('Digite um numero para mostrar sua tabuada: '))

print(f'Tabuada do {num}')
print('-' * 15)

print(f'\033[31m{num} * 1 = {num * 1}')
print(f'{num} * 2 = {num * 2}')
print(f'{num} * 3 = {num * 3}')
print(f'{num} * 4 = {num * 4}')
print(f'{num} * 5 = {num * 5}')
print(f'{num} * 6 = {num * 6}')
print(f'{num} * 7 = {num * 7}')
print(f'{num} * 8 = {num * 8}')
print(f'{num} * 9 = {num * 9}')
print(f'{num} * 10 = {num * 10}\033[m')

print('-' * 15)