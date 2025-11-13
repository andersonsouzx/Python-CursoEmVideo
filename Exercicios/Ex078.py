''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

numbers = []

for n in range(0, 5):
    numbers.append(int(input(f'Digite um valor para a posição {n}: ')))

print('=-' * 25)
print(f"Você digitou os valores {', '.join(map(str, numbers))}") # removendo colchetes e vírgulas

print(f'O maior valor digitado foi {max(numbers)} nas posições ', end='')
for indice, valor in enumerate(numbers): #iterando sobre o indice e o valor da lista
    if valor == max(numbers):
        print(f'{indice}... ', end='')

print(f'\nO menor valor digitado foi {min(numbers)} nas posições ', end='')
for indice, valor in enumerate(numbers):
    if valor == min(numbers):
        print(f'{indice}... ', end='')