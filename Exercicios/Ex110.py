# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from Modulos.Ex110 import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 10, 5)