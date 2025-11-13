''' Escreva um programa que pergunte o salário de um funcionário e calcule
 o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para inferiores ou iguais, o aumento é de 15%.  '''

salario = float(input('Qual é seu salário? R$'))

if salario > 1250:
    aumento1 = (salario * 10 / 100) + salario #calcula 10% e soma com salario anterior
    print(f'Seu novo salário será R${aumento1:.2f}')
else:
    aumento2 = (salario * 15 / 100) + salario ##calcula 15% e soma com salario anterior
    print(f'Seu novo salário será R${aumento2:.2f}')