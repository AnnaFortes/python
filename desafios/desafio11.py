#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input('Valor do salário: '))
aumento = int(input('Porcentagem do aumento: '))
conta = (aumento / 100) * salario
novoSalario = salario + conta
print(f'Antigo salário: {salario}\nNovo salário: {novoSalario}')