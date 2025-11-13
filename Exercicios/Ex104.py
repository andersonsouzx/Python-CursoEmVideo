''' Crie um programa que tenha a função leaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n= leiaint('Digite um n')   '''

''' Crie um programa que tenha a função leaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n= leiaint('Digite um n')   '''

def leiaint(n):
    ok = False
    valor = 0

    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            ok = True
            valor = n
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok == True:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')