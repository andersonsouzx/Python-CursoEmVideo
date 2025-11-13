''' INTERACTIVE HELP - help() - acessa informaçoes sobre funcoes
help(input)
print(input.__doc__) - tambem pode ser usado para outras funçoes como print, len...

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

DOCSTRINGS - É uma string (um texto) que serve como documentação oficial de uma função, classe, método ou módulo, após a definição (o def) e deve estar entre aspas triplas (""" """ ou '''  '''), como se fosse um comentário e é chamado usando help(nome_da_função)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Vídeo.
    """ # (param= abreviação de parâmetro)
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

#contador(2, 10, 2)
help(contador)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

PARÂMETROS OPCIONAIS - usado para adicionar uma valor a um param que não tenha sido declarado na chamada da função.

def somar(a=0, b=0, c=0):
    """"""
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor (param= abreviação de parâmetro)
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Vídeo.
    """ # (param= abreviação de parâmetro)
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 5) 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

ESCOPO DE VARIÁVEIS Escopo é a região do código onde uma variável é reconhecida e pode ser acessada. Basicamente, define "onde" uma variável existe.
    1. ESCOPO GLOBAL: Variáveis criadas fora de qualquer função.
    Elas são acessíveis de qualquer lugar do seu script.
    2. ESCOPO LOCAL: Variáveis criadas dentro de uma função.
    Elas só existem e só podem ser usadas *dentro* daquela função.
    Elas são criadas quando a função é chamada e destruídas quando
    a função termina. (exemplo da aula em aula021escopo_var.png)

def testa(b):
# 'global a' avisa a função que o 'a' 
# que ela vai usar é o 'a' do escopo global.
global a  

a = 8     # <-- Modifica o 'a' GLOBAL
b = 4     # <-- 'b' é uma variável LOCAL (só existe aqui dentro)
c = 2     # <-- 'c' é uma variável LOCAL (só existe aqui dentro)
print(f'A (dentro da função) vale: {a}')
print(f'B (dentro da função) vale: {b}')
print(f'C (dentro da função) vale: {c}')

# --- Início do Escopo Global ---
a = 5  # <-- 'a' é uma variável GLOBAL
print(f'A (antes de chamar a função) vale: {a}')

testa(a)  # Chamamos a função

# Como a função usou 'global a', o valor de 'a' foi modificado
print(f'A (fora da função) vale: {a}') 

# As linhas abaixo dariam erro (NameError), 
# pois 'b' e 'c' são locais e não existem aqui fora.
# print(f'B (fora da função) vale: {b}')
# print(f'C (fora da função) vale: {c}')

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

RETORNANDO VALORES - return 
    usada para encerrar a execução de uma função e enviar um valor de volta para o local onde a função foi chamada

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}') '''