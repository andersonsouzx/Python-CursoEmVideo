"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
 e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27 
 (dei uma atualização no código)"""

real = float(input('\033[91mQuanto dinheiro você tem na carteira?\033[m: R$'))
dolar = real / 5.73
euro = real / 6
libra =  real / 7.22 

print(f'Com R$\033[92m{real}\033[m você pode comprar US$\033[95m{dolar:.2f}\033[m €\033[95m{euro:.2f}\033[m e £\033[95m{libra:.2f}\033[m')