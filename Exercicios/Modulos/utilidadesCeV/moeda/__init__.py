def aumentar(preço= 0, taxa= 0, formato= False): # cria um novo param opcional para verficar se o usario quer a formatação
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res) # mosta res normal caso 'formato' seja False ou mostra formatado caso 'formato' seja True.

def diminuir(preço= 0, taxa= 0, formato= False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço= 0, formato= False):
    res = preço * 2
    return res if not formato else moeda(res)
    
def metade(preço= 0, formato= False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço= 0, moeda= 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço=0, aumento=0,  desconto=0):
    print('-' * 35)
    print(f'RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{desconto}% de redução: \t{diminuir(preço, desconto, True)}')
    print('-' * 30)