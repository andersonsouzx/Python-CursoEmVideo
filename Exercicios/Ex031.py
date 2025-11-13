''' Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km 
e R$0.45 para viagens mais longas.  '''

dist = int(input('Digite a distância da viagem em Km: '))

if dist <= 200:
    pc1 = dist * 0.50
    print(f'O valor da passagem foi de R${pc1:.2f}')
else:
    pc2 = dist * 0.45
    print(f'O valor da passagem foi de R${pc2:.2f}')