'''pessoas = {'nome': 'Anderson', 'sexo': 'M', 'idade': 21}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Leandro

pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
--------------------------------------------------------------
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])
--------------------------------------------------------------'''
estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sígla do Estado: ')
    brasil.append(estado.copy()) # fazendo uma copia dos elementos de estado / [:] não funcioina, pois não é possível fazer fatiamentos em dict
for e in brasil:
    '''for v in e.values():
        print(v, end=' ')'''  # mostrando apenas os elementos, ou seja, os estados
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')