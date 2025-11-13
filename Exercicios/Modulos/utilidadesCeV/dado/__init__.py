def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() # tira os espaços
        if entrada.isalpha() or  entrada == '': #... ou se entrada for vazio
            print(f'\033[0;31mERRO! \'{entrada}\' é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)