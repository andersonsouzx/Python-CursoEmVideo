''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primero valor 3.
C) Quais foram os números pares.    '''

numbers = []
pares = []

for i in range(1, 5):
    n = int(input(f'Digite o {i}° número: '))
    numbers.append(n)

numbers_tuple = tuple(numbers)
print(f'Você digitou os valores {numbers_tuple}')
if numbers_tuple.count(9) == 0:
    print('O valor 9 não apareceu')
else:
    print(f'O valor 9 apareceu {numbers_tuple.count(9)} vezes')
if 3 in numbers_tuple:
    print(f'O primeiro 3 apareceu na {numbers_tuple.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for number in numbers_tuple:
    if number % 2 == 0:
        pares.append(number)
print(f'Os valores pares digitados foram {" ".join(map(str, pares))}')