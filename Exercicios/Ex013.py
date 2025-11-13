'''Faça um algoritmo que leia o salário de um funcionário
 e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Digite seu salário: '))
novo = salario + (salario * 0.15)

print(f'Seu novo salário é de R${novo:.2f}.')