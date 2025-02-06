# desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No fina, mostre: a) quantas vezes apareceu o valor 9. b) em que posição foi digitado o primeiro valor 3. c) quais foram os números pares. Se buscar um valor que não existe, tem que dar ERRO
contPar = 0
num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite o útimo número: '))

numTupla = (num, num1, num2, num3)

if 9 in numTupla:
    cont = numTupla.count(9)
    print(f'O valor 9 apareceu {cont} vezes')
if 3 in numTupla:
    print(f'O número 3 apareceu na {numTupla.index(3) + 1}° posição')

print(numTupla)