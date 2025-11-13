""" Escreva um programa que leia um valor em metros 
 e o exiba convertido em centímetros e milímetros   """

mtr = float(input('\033[30mDigite um valor em metros: \033[m'))
cm = mtr * 100
mm = mtr * 1000 

print(f'{mtr} metro(s) equivale a {cm} centímetros')
print(f'{mtr} metro(s) equivale a {mm} milímetros')