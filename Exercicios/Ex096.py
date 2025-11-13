# Faça um programa que tenha uma função chamada área(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

print('  Controle de Terrenos')
print('-' * 25)

def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a} m².')
    
área(largura = float(input('LARGURA (m): ')), 
    comprimento = float(input('COMPRIMENTO (m): ')))

'''
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)
'''