''' Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

- à vista DINHEIRO/CHEQUE: 10% de desconto
- à vista no CARTÃO: 5% de desconto
- em até 2x NO CARTÃO: preço normal
- 3x OU MAIS no cartão: 20% de juros    '''

print(f'{" LOJA DO ANDERSON ":=^40}')#colando um título e centralizando
prod = float(input('Digite o valor da compra: R$'))
print(f'A compra custa R${prod:.2f}\n')
op1 = prod - prod * 0.10
op2 = prod - prod * 0.05
op3 = prod / 2

largura = 50  # Defina a largura desejada para centralizar
print('Tipos de pagamento:'.center(largura))
print(f'''[ 1 ] à vista DINHEIRO/CHEQUE: 10% de desconto = R${op1:.2f}
[ 2 ] à vista no CARTÃO: 5% de desconto = R${op2:.2f}
[ 3 ] em até 2x NO CARTÃO: preço normal = 2x de R${op3:.2f}
[ 4 ] 3x OU MAIS no cartão: 20% de juros\n''')

pag = int(input('Qual será a forma de pagamento? '))
if pag == 1:
    print (f'Ok, você irá pagar R${op1:.2f}')
elif pag == 2:
    print(f'Ok, você irá pagar R${op2:.2f}')
elif pag == 3:
    print(f'Ok, você irá pagar 2x de R${op3:.2f}')
elif pag == 4:
    vez = int(input('Você quer parcelar em quantas vezes? '))
    if vez >= 3:
        parc = (prod + prod * 0.20) / vez
        vprod = prod + prod * 0.20
        print(f'Você irá pagar {vez}x de R${parc:.2f}, totalizando R${vprod:.2f} com 20% de juros.')
    else:
        print('Parcelamento em menos de 3x não é válido nesta condição!')
else:
    print('\033[31mOpção inválida!\033[m')