''' Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.  '''


vel = int(input('Velocidade do carro em Km/h: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você foi multado em R$: {multa:.2f}!')
else:
    print('Siga!')