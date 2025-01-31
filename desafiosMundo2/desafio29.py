cont = 0
soma = 0
num = 0

while num != 999:
    num = int(input('Digite um valor [999 para sair]: '))   
    
    cont += 1
    soma += num

print(f'Ao todo tiveram {cont} números digitados e a soma entre eles é de {soma - 999}')

if num == 999:
        print('ACABOU!')
    
    
    

        




