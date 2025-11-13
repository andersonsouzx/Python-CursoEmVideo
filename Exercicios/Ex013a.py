'''Faça um algoritmo que leia o salário de um funcionário
 e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Digite seu salário: '))
percentual = 15
aumento = salario * (percentual / 100)
novo = salario + aumento

print(f'Seu novo salário é de R${novo:.2f}.')