cont = 0
soma = 0
num = 0

num = int(input('Digite um valor [999 para sair]: '))

while num != 999:
    soma += num
    cont += 1

    num = int(input('Digite um valor [999 para sair]: '))       

print(f'Ao todo tiveram {cont} números digitados e a soma entre eles é de {soma}')

if num == 999:
        print('ACABOU!')
    
    
    

        




