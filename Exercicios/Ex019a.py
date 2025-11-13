'''Um professor quer sortear um dos seus quatro alunos 
 para apagar o quadro. Faça um rograma que ajude ele, 
 lendo o nome deles e escrevendo o nome do escolhido.'''

import random

nome = str(input('Digite o nome dos alunos separado por vírgula: '))
lista = nome.split(', ')
escolhido = random.choice(lista)

print(f'O aluno escolhido foi: {escolhido}')