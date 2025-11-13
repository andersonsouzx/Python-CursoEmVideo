# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from time import sleep

num = 0
opcao = ''
soma = 0
media = 0
count = 0
allnum = [] # Lista para guardar todos os números e depois verificar maior e menor

while True:
    num = int(input('Digite um número: '))
    
    while True:
        opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if opcao in ['S','N']:
            break # Só sai da validação se a entrada for válida
        print('Opção inválida. Tente novamente.\n')

    soma += num
    count += 1
    allnum.append(num)
    
    if opcao == 'N':
        break

media = soma / count
print('\nCalculando resultado. Aguarde...')
sleep(3)
print('-='*15)
sleep(2)
print(f'Foram digitados {count} números, tendo soma {soma} e média {media:.2f}.')
print(f'O maior valor foi {max(allnum)} e o menor foi {min(allnum)}.')
print('\nFim.')