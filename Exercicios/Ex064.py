# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from time import sleep

num = 0
count = 0           # num = count = soma = 0
soma = 0
flag = 999

while num != flag:
    num = int(input('Digite um número [999 para parar]: '))

    if num == 999:
        print('\nFinalizando...')
        sleep(2)
        break

    soma += num
    count += 1

print(f'Foram digitados {count} números, e a soma entre eles foi {soma}.')
print('FIM.')