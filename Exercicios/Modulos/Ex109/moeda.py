def aumentar(preço= 0, taxa= 0, formato= False): # cria um novo param opcional para verficar se o usario quer a formatação
    res = preço + (preço * taxa/100)
    return res if formato == False else moeda(preço) # mosta res normal caso 'formato' seja False ou mostra formatado caso 'formato' seja True.

def diminuir(preço= 0, taxa= 0, formato= False):
    res = preço - (preço * taxa/100)
    return res if formato == False else moeda(preço)

def dobro(preço= 0, formato= False):
    res = preço * 2
    return res if formato == False else moeda(preço)
    
def metade(preço= 0, formato= False):
    res = preço / 2
    return res if formato == False else moeda(preço)

def moeda(preço= 0, moeda= 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

# https://www.youtube.com/watch?v=Y0zNYTHoGhQ