''' Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.'''

list_num = []

for c in range(1, 6):
    n = int(input(f'Digite o {c}° valor: '))

    if c == 1 or n > list_num[-1]:
        list_num.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(list_num):
            if n <= list_num[pos]:
                list_num.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {list_num}')