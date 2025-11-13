''' Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes   '''

''' Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo. '''

a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))

if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo!')
    if a == b and b == c:
        print('Triângulo Equilátero, todos os lados são iguais.')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles, dois lados são iguais.')
    else:
        print('Triângulo Escaleno, todos os lados são diferentes.')
else:
    print('Não é possível formar um triângulo!')