nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[31mREPROVADO!\033[m')
elif media >= 5.1 and media < 6.0:
    print('\033[33mRECUPERAÇÃO!\033[m')
else:
    print('\033[32mAPROVADO!\033[m')