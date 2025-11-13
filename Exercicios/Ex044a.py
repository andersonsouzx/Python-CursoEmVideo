''' Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

- à vosta DINHEIRO/CHEQUE: 10% de desconto
- à vista no CARTÃO: 5% de desconto
- em até 2x NO CARTÃO: preço normal
- 3x OU MAIS no cartão: 20% de juros    '''

print(f'{"LOJA DO ANDERSON":=^40}')
compra = float(input('Digite o valor da compra: R$'))

print('''CONDIÇÃO DE PAGAMENTO:
[ 1 ] à vosta DINHEIRO/CHEQUE: 10% de desconto
[ 2 ] à vista no CARTÃO: 5% de desconto
[ 3 ] em até 2x NO CARTÃO: preço normal
[ 4 ] 3x OU MAIS no cartão: 20% de juros ''')
opcao = int(input('Qual será forma de pagamento? '))
if opcao == 1:
    valor = compra - compra * 0.10
    print(f'A compra de R${compra:.2f} terá 10% de desconcoto, ficando R${valor:.2f}.')
elif opcao == 2:
    valor = compra - compra * 0.05
    print(f'A compra de R${compra:.2f} terá 5% de desconcoto, ficando R${valor:.2f}.')
elif opcao == 3:
    parc = compra / 2
    print(f'A compra de R${compra:.2f} ficará 2x de R${parc}.')
elif opcao == 4:
    vez = int(input('Você quer parcelar em quantas vezes? '))
    if vez < 3:
        print("Essa opçao é somente para pagamentos em mais de 3x.")
    else:
        parc = (compra * 0.20) / vez
        valor = compra + compra * 0.20
        print(f'A compra de R${compra:.2f} parcelada em {vez}x ficará {vez}x de R${parc:.2f}, totalizando R${valor:.2f} ')
else:
    print('Opção inválida!')