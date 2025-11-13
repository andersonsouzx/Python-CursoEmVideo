''' Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.    '''

from time import sleep

soma = 0
multiplicacao = 0
maior = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Agora o segundo valor: '))

while True:
    print('''        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
        print('=-=' * 15)
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicacao}.')
        print('=-=' * 15)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2} o maior valor é {maior}.')
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}.')
        print('=-=' * 10)
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Agora o segundo valor: '))
        print('=-=' * 10)
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        break
    else:
        print('Opção inválida. Tente novamente!')

print('=-=' * 10)
print('Fim do programa! Volte sempre!')