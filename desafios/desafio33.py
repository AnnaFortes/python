#pergunte o salario e calcule o valor do aumento, salario superior a 1.250 aumento de 10%, inferiores aumento de 15%
salario = float(input('Digite o valor do salário: '))
if salario < 1.250:
    aumento = 10 / 100
    nSalario = salario + (salario * aumento)
    print(f'O novo salário é {nSalario :.2f} reais')
else: 
    aumento2 = 15 / 100
    nvSalario = salario + (salario * aumento2)
    print(f'O novo salário é {nvSalario :.2f}')
