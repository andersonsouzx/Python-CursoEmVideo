''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.  '''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numuser = int(input('Digite um número entre 0 e 20: '))
    if  0 <= numuser <= 20:#if numuser >= 0 and numuser <= 20 (verifica se numuser estiver entre 0 e 20)
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {(num[numuser])}')