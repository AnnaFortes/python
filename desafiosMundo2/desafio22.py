sexo = ''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #pegando somente a primeira letra
while sexo not in ('M', 'F'):
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
   
        
    

