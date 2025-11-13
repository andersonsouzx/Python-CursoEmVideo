# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Digite um numero para mostrar sua tabuada: '))
for i in range (1, 11):
    print(f'{num} x {i} = {num * i}')


'''num = int(input('Digite um numero para mostrar sua tabuada: '))
larg = 40

print('-='*15)
print(f'TABUADA DO {num}'.center(larg))

for i in range (1, 11):
    mult = num * i
    print(f'{num} x {i} = {mult}')

print('-='*15)
'''