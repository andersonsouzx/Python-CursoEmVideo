''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:

- 1 para BINÁRIO
- 2 para OCTAL
- 3 para HEXADECIMAL    '''

num = int(input('Digite um número inteiro qualquer: '))

print('''\nEscolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
base = int(input('Sua opção: '))
print('')

if base == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida!')