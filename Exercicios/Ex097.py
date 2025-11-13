''' Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

Ex:
escreva('Olá, Mundo!')

Saída:
-------------
 Olá, Mundo!
------------
'''
def escreva(msg):
    print('~' * (len(msg) + 4))#aqui, o '+4' está sendo usado para deixar a mensagem no centro dos '~', com dois a esquerda e dois a direita.
    print(f'  {msg}')
    print('~' * (len(msg) + 4))

escreva('Gusatavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')