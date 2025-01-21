#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média entre \033[32m {nota1}\033[m  e \033[32m {nota2}\033[m  é: \033[34m {media :.1f}\033[m ')