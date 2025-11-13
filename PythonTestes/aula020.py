'''
def linha():
    print('-' * 30)

linha()
print('CURSO EM VÍDEO')
linha()
print('PYTHON')
linha()
-----------------------------------------------------------------
def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
-----------------------------------------------------------------
def soma(a, b):
print(f'A = {a} e B = {b}')
s = a + b
print(f'A soma de A + B = {s}')

soma(4, 5)
soma(b=int(input('Digite A: ')), a= int(input('Digite B: ')))
-----------------------------------------------------------------
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for valor in num:
        print(valor, end=' ')
    print('FIM!')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
-----------------------------------------------------------------'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+= 1

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)