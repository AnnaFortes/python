#faça um programa que leia um numero inteiro e mostre sua tabuada 
numero = int(input('Digite um número: '))
print('=' * 12)

for i in range(1, 11, 1): #não era preciso colocar o 1 pois já é o padrão
     r = numero * i
     print(f'{numero} x {i:2} = \033[32m {r}\033[m ')

print('=' * 12)