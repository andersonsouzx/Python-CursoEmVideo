n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print(f'Sua média foi de {m:.1f}')
print('media boa' if m>=6 else 'media ruim')
'''if m >=6:
    print('média boa')
else:
    print('média ruim')'''