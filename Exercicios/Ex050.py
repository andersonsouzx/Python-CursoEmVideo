# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-0.

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Foram encontrados {cont} valores pares e a soma deu {soma}.')