'''num = [2, 5, 9, 1]
num[2] = 3 # alterando o valor do indíce dois de 9 para 3
num.append(7) # adicionando 7 ao final da lista
num.sort() # deixa a lista em ordem crescente
num.sort(reverse=True) # alterando a lista para ordem decrescente
num.insert(2, 0) # inserindo na posição 2 o valor 0
num.pop() # remove o ultimo valor da lista
num.pop(2) # remove o valor do indíce 2
num.remove(3) # elimina o valor desejado
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
for count in range(1, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.') '''

a = [2, 3, 4, 7]
b = a[:] # fazendo uma copia de a dentro de b
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')