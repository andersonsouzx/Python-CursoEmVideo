# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sortando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush= True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)