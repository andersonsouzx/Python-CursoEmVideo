# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

print('-' * 25)
def fatorial(num, show):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c                       # f = f * c
        if show:                     # if show == True:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f

print(fatorial(5, True))
help(fatorial)