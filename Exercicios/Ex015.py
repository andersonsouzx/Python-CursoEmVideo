'''Escreva um programa que pergunte a quantidade de Km percorridos
 por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km
 rodado.
'''

km = float(input('Quantidade de km percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado: '))
pdia = dias * 60
pkm = km * 0.15
total = pdia + pkm

print(f'Você pagará R${pdia:.2f} pelos dias alugados e R${pkm:.2f} por km percorrido.')
print(f'O valor total foi de R${total:.2f}')