#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print(f'\nO dobro de \033[36m{n}\033[m é {n*2}')
print(f'O triplo de \033[36m{n}\033[m é {n*3}')
print(f'A raiz quadrada de \033[36m{n}\033[m é {n**(1/2):.1f}')