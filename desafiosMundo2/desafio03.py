num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print(f'O primeiro valor é maior que o segundo, {num1} > {num2}')
elif num2 > num1:
    print(f'O segundo valor é maior que primeiro, {num2} > {num1}')
else:
    print(f'Não existe maior valor entre {num1} e {num2}, ambos são iguais!')