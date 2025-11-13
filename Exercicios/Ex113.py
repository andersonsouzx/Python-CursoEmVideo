# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mErro! digite um valor inteiro válido.\033[m')
            continue # volta desde o while true
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mErro! digite um valor real válido.\033[m')
            continue
        else:
            return n

numInt = leiaInt('Digite um valor inteiro: ')
numFloat = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat}.')