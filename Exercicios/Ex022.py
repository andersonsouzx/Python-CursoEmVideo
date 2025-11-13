'''  Crie um programa que leia o nome completo de uma pessoa e mostre:
🔵 O nome com todas as letras maiúsculas.
🔵 O nome com todas minúsculas.
🔵 Quantas letras ao todo (sem considerar espaços).
🔵 Quantas letras tem o primeiro nome.  ''' 

nome = str(input('Digite seu nome completo: ')).strip() #eliminar espaços
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúscuas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {nome.find(' ')} letras')