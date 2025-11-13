'''O mesmo professor do desafio anterior quer sortear 
 a ordem de apresentação de trabalhos dos alunos. 
 Faça um programa que leia o nome dos quatro alunos 
 e mostre a ordem sorteada.'''

from random import shuffle
nome = str(input('Digite o nome dos alunos separado por vírgula: '))
lista = nome.split(', ')
shuffle(lista)

print(f'A ordem sorteada foi: {lista}')
