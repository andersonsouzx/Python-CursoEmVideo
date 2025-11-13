# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
''' Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA BOLO
ANOTARAM A DATA DA MARATONA '''

frase = str(input('Digite uma frase: ')).upper().replace(' ','')
frase_invert = frase [::-1]

print(f'O iverso de {frase} é {frase_invert}')

if frase == frase_invert:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndrmo!')