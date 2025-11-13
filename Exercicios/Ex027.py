''' Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza  '''

nome = str(input('Digite seu nome completo: '))
n = nome.split()
print(f'Primeiro = {n[0]}')
print(f'último = {n[-1]}')