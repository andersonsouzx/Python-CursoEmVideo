# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
for i in range(1,11):
    pa= n + r * i
    print(pa, end=' -> ')

'''primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão:'))
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print(i, end=' -> ')
print('ACABOU')'''