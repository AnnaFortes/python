#faça um programa que leia a largura e a altura de uma parede, calcule sua area e a quantidade necessaria de tinta para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2
largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

area = largura * altura  
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura :.1f} x {altura :.1f} e sua área é de {area :.1f}m²')
print(f'A quantidade de tinta necessária para pintar a parede é de {tinta} litros')