n = 0
count = 0

while count < 5:
    n = int(input(f'Você tem {5 - count} tentativas para acertar o número: '))
    count += 1

    if n == 999:
        print('Parabéns, você acertou!')
        break
        
if n != 999:
    print('Infelizmente você não acertou')

print('FIM')