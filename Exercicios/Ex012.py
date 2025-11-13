"""Faça um algoritmo que leia o preço de um produto
 e mostre seu novo preço, com 5% se desconto."""

preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
novo = preco - desconto

print(f'O novo valor do produto é R${novo:.2f}')