''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 O programa vai perguntar VALOR DA CASA, o SALÁRIO do comprador 
 e em QUANTOS ANOS ele vai pagar.
 
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado.   '''

casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o salário do comprador: R$'))
anos = int(input('Em quanto anos de financiamento? '))
mes = anos * 12
pres = casa / mes
#pres = casa / (ano * 12) /// mesmo modo, mas sem criar uma variavel mes
minimo = sal * 0.30

if pres <= minimo:
    aprovado = 'APROVADO'
else:
    aprovado = 'NEGADO'

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${pres:.2f} e o empréstimo foi {aprovado}')