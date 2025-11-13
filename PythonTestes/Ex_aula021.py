'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

print()
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados foram {f1}, {f2} e {f3}')'''

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num): # if par(num) == True:
    print(f'{num} é par.')
else:
    print(f'{num} é ímpar.')