"""Faça um algoritmo que leia o preço de um produto
 e mostre seu novo preço, com 5% se desconto."""

preco = float(input('Digite o preço do produto: '))
porcentagem = int(input('Digite o valor do desconto: '))
desconto = preco * (porcentagem / 100)
valor = preco - desconto

print(f'O novo valor do produto é R${valor:.2f}.')