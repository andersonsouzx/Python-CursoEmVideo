"""Faça um programa que leia a largura e a altura de uma parede em metros,
 calcule a sua área e a quantidade de tinta necessária para pintá-la,
   sabendo que cada litro de tinta pinta uma área de 2m²."""

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = larg * alt
tinta = area / 2

print(f"Sua parede tem uma dimensão de {larg}x{alt} e sua área é de {area}m².")
print(f'Você precisará de {tinta} litros de tinta para pintar a parede')