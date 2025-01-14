#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
cato = int(input('Digite o valor do cateto oposto: '))
cata = int(input('Digite o valor do cateto adjacente: '))
res = cato ** 2 + cata ** 2
raiz = sqrt(res)
print(f'A hipotenusa é {raiz :.1f}')