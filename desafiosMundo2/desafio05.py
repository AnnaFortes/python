nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4.9:
    print(f'Com as notas {nota1 :.1f} e {nota2 :.1f} a média foi {media :.1f} e o aluno foi \033[31mREPROVADO!\033[m')
elif 6.9 <= media >= 5.0: 
# ou and media <= 6.9:
    print(f'Com as notas {nota1 :.1f} e {nota2 :.1f} a média foi {media :.1f} e o aluno está em \033[33mRECUPERAÇÃO!\033[m')
else:
    print(f'Com as notas {nota1 :.1f} e {nota2 :.1f} a média foi {media :.1f} e o aluno foi \033[32mAPROVADO!\033[m')