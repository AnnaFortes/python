cont = soma = 0

while True:
    num = int(input('Digite um número: [999 para parar] '))

    if num == 999:
        break  

    cont += 1  
    soma += num
     
print(f'No total tivemos {cont} números digitados e a soma entre eles foi de {soma} ')
