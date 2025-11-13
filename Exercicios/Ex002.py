''' Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''

nome = (input("Digite seu nome: "))
if nome == "Anderson":
    print('Belo nome!')
else:
    print(f"É um prazer te conhecer \033[32m{nome}\033[m")