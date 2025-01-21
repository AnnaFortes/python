salario = float(input('\nDigite o valor do salário: '))
if salario < 1.250:
    novoSalario = salario + (salario * 15 / 100)
else: 
    novoSalario = salario + (salario * 10 / 100)

print(f'O novo salário é R${novoSalario :.2f}')
