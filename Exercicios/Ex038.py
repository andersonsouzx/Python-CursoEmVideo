''' Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são IGUAIS    '''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número:'))

if num1 > num2:
    print('O primeiro valor é MAIOR')
elif num1 < num2:
    print('O segundo valor é MAIOR')
else:
    print('Não existe valor maior, os dois são IGUAIS')