''' Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobra() e metade().

    Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from Modulos.Ex107 import moeda
# from moeda import metade, dobro, aumentar, diminuir e retira moeda.[...]

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(p, 13)}')