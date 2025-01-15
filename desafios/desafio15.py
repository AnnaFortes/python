#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
hipo = cato ** 2 + cata ** 2
raiz = sqrt(hipo)
print(f'A hipotenusa vai medir {raiz :.2f}')