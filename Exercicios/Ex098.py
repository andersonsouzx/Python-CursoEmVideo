''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.  '''


# USANDO FOR
'''from time import sleep

def contador(início, fim, passo):
    print('-=' * 15)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1

    if início < fim:
        for i in range(início, fim + 1, passo):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for i in range(início, fim - 1, -passo):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

---------------------------------------------------------------------------------'''
from time import sleep

def contador(início, fim, passo):

    if passo < 0:
        passo *= -1 #transformando um num negativo em positivo
    if passo == 0:
        passo = 1 # se p for 0 ele recebe o valor 1

    print('-=' * 15)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2)

    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont} ', end='', flush= True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont} ', end='', flush= True)
            sleep(0.5)
            cont -= passo
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
#contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
i = int(input('Início:  '))
f = int(input('Fim:     '))
p = int(input('Passo:   '))
contador(i, f, p)

# Usa flush=True (51, 58) para forçar a exibição imediata do print() antes do sleep(), já que o end=' ' impede a quebra de linha.