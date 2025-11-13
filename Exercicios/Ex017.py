"""Faça um programa que leia o comprimento do cateto oposto
 e do cateto adjacente de um triângulo retângulo, 
 calcula e mostre o comprimento da hipotenusa."""

from math import hypot
cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input ('Digite o comprimento do cateto adjascente: '))
hipot = hypot(cat_o, cat_a)

print(f'O comprimento da hipotenusa é: {hipot:.2f}')