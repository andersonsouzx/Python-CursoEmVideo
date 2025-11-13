''' Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo. '''

a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))

if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')